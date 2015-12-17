import unittest
import day8


class Day8_GetNumCodeCharsForStringTests(unittest.TestCase):
    
    def test_empty_string_in_quotes(self):
        input_str = r'""'
        result = day8.get_num_code_chars(input_str)
        self.assertEqual(2, result)

    def test_quoted_chars_only(self):
        input_str = r'"abc"'
        result = day8.get_num_code_chars(input_str)
        self.assertEqual(5, result)
        
    def test_string_with_escaped_quote(self):
        input_str = r'"aaa\"aaa"'
        print input_str
        result = day8.get_num_code_chars(input_str)
        self.assertEqual(10, result)
        
    def test_test(self):
        input_str = r'"\x27"'
        print input_str
        result = day8.get_num_code_chars(input_str)
        self.assertEqual(6, result)
    

class Day8_GetNumStringCharsForStringTests(unittest.TestCase):
    
    def test_empty_string(self):
        input_str = r'""'
        result = day8.get_num_str_chars(input_str)
        self.assertEqual(0, result)

    def test_quoted_chars_only(self):
        input_str = r'"abc"'
        result = day8.get_num_str_chars(input_str)
        self.assertEqual(3, result)
        
    def test_string_with_escaped_quote(self):
        input_str = r'"aaa\"aaa"'
        print input_str
        result = day8.get_num_str_chars(input_str)
        self.assertEqual(7, result)
        
    def test_test(self):
        input_str = r'"\x27"'
        print input_str
        result = day8.get_num_str_chars(input_str)
        self.assertEqual(1, result)
    
    def test_trailing_slash(self):
        input_str = r'"\\xa8br\\x8bjr\\""'
        print input_str
        result = day8.get_num_str_chars(input_str)
        self.assertEqual(14, result)
        

class Day8_getNumCodeOverheadCharsTests(unittest.TestCase):
    
    def test_example(self):
        input_strs = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
        code_chars = sum([day8.get_num_code_chars(s) for s in input_strs])
        str_chars = sum([day8.get_num_str_chars(s) for s in input_strs])
        self.assertEqual(23, code_chars)
        self.assertEqual(11, str_chars)
        self.assertEqual(12, code_chars - str_chars)

class Day8_encodeCharsTests(unittest.TestCase):

    # def test_0(self):
    #     result = day8.encode_chars('\\"')
    #     expect = r'"\\\""'
    #     print len(expect)
    #     self.assertEqual(expect, result)
        
    def test_1(self):
        result = day8.encode_chars(r'""')
        expect = r'"\"\""'
        print 'Expect: %r' % expect
        print 'Result: %r' % result
        self.assertEqual(expect, result)
    
    def test_2(self):
        result = day8.encode_chars(r'"abc"')
        expect = r'"\"abc\""'
        print 'Expect: %r' % expect
        print 'Result: %r' % result
        self.assertEqual(expect, result)

    def test_3(self):
        result = day8.encode_chars(r'"aaa\"aaa"')
        expect = r'"\"aaa\\\"aaa\""'
        print 'Expect: %r' % expect
        print 'Result: %r' % result
        self.assertEqual(expect, result)

    def test_4(self):
        result = day8.encode_chars(r'"\x27"')
        expect = r'"\"\\x27\""'
        print 'Expect: %r' % expect
        print 'Result: %r' % result
        self.assertEqual(expect, result)

class Day8_getNumEncodedCharsTests(unittest.TestCase):
    
    def test_empty_string(self):
        input_str = r'""'
        result = day8.get_num_encoded_chars(input_str)
        self.assertEqual(6, result)

    def test_chars_only_string(self):
        input_str = r'"abc"'
        result = day8.get_num_encoded_chars(input_str)
        self.assertEqual(9, result)

    def test_escaped_quote(self):
        input_str = r'"aaa\"aaa"'
        result = day8.get_num_encoded_chars(input_str)
        self.assertEqual(16, result)

    def test_hex(self):
        input_str = r'"\x27"'
        result = day8.get_num_encoded_chars(input_str)
        self.assertEqual(11, result)


# from day8 import get_num_code_chars, get_num_str_chars, get_num_encoded_chars, INPUT_STRING

# words = INPUT_STRING.split('\n')
# # part 1
# total_code_chars = sum([get_num_code_chars(s) for s in words])
# total_str_chars = sum([get_num_str_chars(s) for s in words])
# print '%s - %s = %s' % (total_code_chars, total_str_chars, \
#     total_code_chars-total_str_chars)

# # part 2
# total_encoded_chars = sum([get_num_encoded_chars(s) for s in words])
# print 'Part 2'
# print '%s - %s = %s' % (total_encoded_chars, total_code_chars, \
#     total_encoded_chars - total_code_chars)
# # 1461 - too low
# # 2117

import unittest
import day10

class Day10_LookAndSayTests(unittest.TestCase):

    def test_single_digit(self):
        input_string = "1"
        expect = "11"
        self.assertEqual(expect, day10.look_and_say(input_string))
    
    def test_two_consecutive_digits(self):
        input_string = "11"
        expect = "21"
        self.assertEqual(expect, day10.look_and_say(input_string))
    
    def test_two_different_digits(self):
        input_string = "21"
        expect = "1211"
        self.assertEqual(expect, day10.look_and_say(input_string))
    
    def test_multiple_digits_1(self):
        input_string = "1211"
        expect = "111221"
        self.assertEqual(expect, day10.look_and_say(input_string))
    
    def test_multiple_digits_2(self):
        input_string = "111221"
        expect = "312211"
        self.assertEqual(expect, day10.look_and_say(input_string))
    
    def test_three_unique_digits(self):
        input_string = "3333113322"
        expect = "43212322"
        self.assertEqual(expect, day10.look_and_say(input_string))

class Day10_GenerateNextChunkTests(unittest.TestCase):
    
    # Cut to the chase.
    def test_split_input_with_three_unique_digits(self):
        input_string = "3333113322"
        expected = ["3333", "11", "33", "22"]
        result = []
        for yielded in day10.generate_chunks(input_string):
            result.append(yielded)
        self.assertEqual(expected, result)


# Day 10
# import day10
# my_string = "1113222113"
# for i in range(50):
#     my_string = day10.look_and_say(my_string)
# print len(my_string)
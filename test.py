import unittest
from day3 import get_num_houses_visited, split_instructions, get_total_houses_visited_with_robo_santa
from day4 import get_suffix_num_resulting_in_five_zeroes, get_suffix_num_resulting_in_six_zeroes
from day5 import is_nice, is_nice_2, INPUT_STRING
import day7
import day8
import day9

class Day3_numHousesVisitedTests(unittest.TestCase):

    def test_two_houses(self):
        input_string = ">"
        self.assertEqual(2, get_num_houses_visited(input_string))

    def test_square(self):
        input_string = "^>v<"
        self.assertEqual(4, get_num_houses_visited(input_string))

    def test_back_and_forth(self):
        input_string = "^v^v^v^v^v"
        self.assertEqual(2, get_num_houses_visited(input_string))

class Day3_splitDirectionsTests(unittest.TestCase):

    def test_1(self):
        input_string = "^v"
        santa, robo = split_instructions(input_string)
        self.assertEqual("^", santa)
        self.assertEqual("v", robo)

    def test_2(self):
        input_string = "^>v<"
        santa, robo = split_instructions(input_string)
        self.assertEqual("^v", santa)
        self.assertEqual("><", robo)

    def test_3(self):
        input_string = "^v^v^v^v^v"
        santa, robo = split_instructions(input_string)
        self.assertEqual("^^^^^", santa)
        self.assertEqual("vvvvv", robo)

class GetNumHousesVisitedWithRoboSantaTests(unittest.TestCase):
    def test_1(self):
        input_string = "^v"
        self.assertEqual(3, get_total_houses_visited_with_robo_santa(input_string))

    def test_2(self):
        input_string = "^>v<"
        self.assertEqual(3, get_total_houses_visited_with_robo_santa(input_string))

    def test_3(self):
        input_string = "^v^v^v^v^v"
        self.assertEqual(11, get_total_houses_visited_with_robo_santa(input_string))

class Day4Tests(unittest.TestCase):

    def test_1(self):
        key = 'abcdef'
        result = get_suffix_num_resulting_in_five_zeroes(key)
        self.assertEqual(609043, result)
        
    def test_2(self):
        key = 'pqrstuv'
        result = get_suffix_num_resulting_in_five_zeroes(key)
        self.assertEqual(1048970, result)
    
    def test_puzzle_2(self):
        key = 'iwrupvqb'
        result = get_suffix_num_resulting_in_six_zeroes(key)
        self.assertEqual(9958218, result)

class Day5Tests(unittest.TestCase):
    
    def test_nice_1(self):
        self.assertTrue(is_nice("ugknbfddgicrmopn"))
    def test_nice_2(self):
        self.assertTrue(is_nice("aaa"))
        
    def test_naughty_1(self):
        self.assertFalse(is_nice("jchzalrnumimnmhp"))
    def test_naughty_2(self):
        self.assertFalse(is_nice("haegwjzuvuyypxyu"))
    def test_naughty_3(self):
        self.assertFalse(is_nice("dvszwmarrgswjxmb"))
    


class Day5Part2Tests(unittest.TestCase):
    
    def test_1(self):
        self.assertTrue(is_nice_2("qjhvhtzxzqqjkmpb"))
     
    def test_2(self):
        self.assertTrue(is_nice_2("xxyxx"))

    def test_3(self):
        self.assertFalse(is_nice_2("uurcxstgmygtbstg"))
        
    def test_4(self):
        self.assertFalse(is_nice_2("ieodomkazucvgmuy"))
        
    def test_overlap_doesnt_count(self):
        self.assertFalse(is_nice_2("aaa"))


from day6 import convert_instruction_string, apply_action_to_value, apply_instruction_to_grid, apply_instruction_string_to_grid, get_1000_by_1000_grid, get_num_lights_on, get_brightness

class Day6_convertInstructionStringTests(unittest.TestCase):
    
    def test_convert_instruction_turn_off(self):
        example = "turn off 387,19 through 720,700"
        expected = "turn off", (387, 19), (720, 700)
        self.assertEqual(expected, convert_instruction_string(example))

    def test_convert_instruction_turn_on(self):
        example = "turn on 952,417 through 954,845"
        expected = "turn on", (952,417), (954,845)
        self.assertEqual(expected, convert_instruction_string(example))

    def test_convert_instruction_toggle(self):
        example = "toggle 347,482 through 959,482"
        expected = "toggle", (347,482), (959,482)
        self.assertEqual(expected, convert_instruction_string(example))

class Day6_applyActionToValueTests(unittest.TestCase):
    
    def test_turn_on(self):
        result = apply_action_to_value("turn on", 0)
        self.assertEqual(1, apply_action_to_value("turn on", 0))
        self.assertEqual(2, apply_action_to_value("turn on", 1))
    
    def test_turn_off(self):
        self.assertEqual(0, apply_action_to_value("turn off", 0))
        self.assertEqual(0, apply_action_to_value("turn off", 1))
        self.assertEqual(4, apply_action_to_value("turn off", 5))
    
    def test_toggle(self):
        self.assertEqual(2, apply_action_to_value("toggle", 0))
        self.assertEqual(3, apply_action_to_value("toggle", 1))
        

class Day6_applyInstructionToGridTests(unittest.TestCase):
    
    def test_turn_on(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        instruction = "turn on", (0, 0), (3, 2)
        expected = [
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0]
        ]
        result = apply_instruction_to_grid(grid, instruction)
        self.assertEqual(expected, result)

    def test_turn_off(self):
        grid = [
            [0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0]
        ]
        instruction = "turn off", (2, 0), (3, 1)
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0]
        ]
        result = apply_instruction_to_grid(grid, instruction)
        self.assertEqual(expected, result)

class Day6_GetNumLightsOn(unittest.TestCase):
    def test_all_zeroes(self):
        grid = get_1000_by_1000_grid()
        self.assertEqual(0, get_num_lights_on(grid))
    
    def test_example(self):
        grid = [
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
        self.assertEqual(9, get_num_lights_on(grid))

    def test_example_full(self):
        grid = [[1 for _ in xrange(1000)] for _ in xrange(1000)]
        self.assertEqual(1000000, get_num_lights_on(grid))

class Day6_getBrightnessTests(unittest.TestCase):
    def test_brightness(self):
        example = [
            [1, 2, 3, 0, 0],
            [3, 3, 3, 3, 0],
            [0, 0, 0, 0, 1]]
        expected = 19
        result = get_brightness(example)
        self.assertEqual(expected, result)

class Day7_CircuitTests(unittest.TestCase):
    
    def test_example_circuit(self):
        circuit = day7.Circuit("""123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""")
        expected = {
            'x': '123',
            'y': '456',
            'd': ('AND', ['x', 'y']),
            'e': ('OR', ['x', 'y']),
            'f': ('LSHIFT', ['x', '2']),
            'g': ('RSHIFT', ['y', '2']),
            'h': ('NOT', [None, 'x']),
            'i': ('NOT', [None, 'y'])
        }
        self.assertEqual(expected, circuit.circuit)
    
    def test_wire_to_wire(self):
        circuit = day7.Circuit("""123 -> x
456 -> y
x -> z""")
        expected = {
            'x': '123',
            'y': '456',
            'z': 'x'}
        self.assertEqual(expected, circuit.circuit)
    
    def test_values_as_gate_inputs(self):
        circuit = day7.Circuit("""123 -> x
456 AND x -> y""")
        expected = {
            'x': '123',
            'y': ('AND', ['456', 'x'])}
        self.assertEqual(expected, circuit.circuit)

# TODO re-add unit tests for Day 7? Ended up refactoring w/o TDD...

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
        
class Day9_MapDistances_Tests(unittest.TestCase):

    def test_convert_input_to_lookup_table(self):
        input_string = """A to B = 3
A to C = 2
A to B = 3
B to C = 5
B to D = 4
C to D = 3"""
        expect = {
            'A': {'B': 3, 'C': 2},
            'B': {'A': 3, 'C': 5, 'D': 4},
            'C': {'A': 2, 'B': 5, 'D': 3},
            'D': {'B': 4, 'C': 3}
        }
        result = day9.map_distances(input_string)
        self.assertEqual(expect, result)
    
    def test_example_map_distances(self):
        i = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
        expect = {
            'London': {'Dublin': 464, 'Belfast': 518},
            'Belfast': {'London': 518, 'Dublin': 141},
            'Dublin': {'Belfast': 141, 'London': 464}}
        self.assertEqual(expect, day9.map_distances(i))


class Day9_GetAllPathsFromAToB_Tests(unittest.TestCase):
    
    def test_get_all_paths_from_single_node(self):
        input_string = """A to B = 3
A to C = 2
A to B = 3
B to C = 5
B to D = 4
C to D = 3"""
        graph = day9.map_distances(input_string)
        expected_paths = [['C', 'A', 'B'], ['C', 'B'], ['C', 'D', 'B']]
        self.assertEqual(expected_paths, day9.get_all_paths_from_a_to_b('C', 'B', graph))
    
    def test_get_all_paths_through_multiple_nodes(self):
        input_string = """A to B = 3
A to C = 2
A to B = 3
B to C = 5
B to D = 4
C to D = 3"""
        graph = day9.map_distances(input_string)
        expected_paths = [['A', 'B', 'C', 'D'], ['A', 'C', 'B', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
        results = day9.get_all_paths_from_a_to_b('A', 'D', graph)
        self.assertTrue(all([expect in results for expect in expected_paths]))
        self.assertTrue(all([result in expected_paths for result in results]))

class Day9_GetLengthOfPath_Tests(unittest.TestCase):
    
    def setUp(self):
        super(Day9_GetLengthOfPath_Tests, self).setUp()
        input_string = """A to B = 3
A to C = 2
A to B = 3
B to C = 5
B to D = 4
C to D = 3"""
        self.graph = day9.map_distances(input_string)
    
    def test_get_length_between_connected_nodes(self):
        result = day9.get_length_of_path(['A', 'B'], self.graph)
        self.assertEqual(3, result)
    
    def test_get_length_of_longer_path(self):
        result = day9.get_length_of_path(['A', 'C', 'B', 'D'], self.graph)
        self.assertEqual(2+5+4, result)

import mock
class Day9_GetShortestPathTests(unittest.TestCase):
    
    def setUp(self):
        input_string = """A to B = 3
A to C = 2
A to B = 3
B to C = 5
B to D = 4
C to D = 3"""
        self.graph = day9.map_distances(input_string)

    def test_gets_shortest_path(self):
        result_path, result_dist = day9.get_shortest_complete_path(self.graph)
        self.assertEqual(8, result_dist)
    
    def test_advent_puzzle(self):
        advent_graph = day9.map_distances(day9.INPUT_STRING)
        result_path, result_dist = day9.get_shortest_complete_path(advent_graph)
        print result_path
        print result_dist
    
    def test_advent_puzzle_part_2_longest_path(self):
        advent_graph = day9.map_distances(day9.INPUT_STRING)
        result_path, result_dist = day9.get_longest_complete_path(advent_graph)
        print result_path
        print result_dist


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

import day11

class Day11_GenerateNextPasswordTests(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual("abcdffaa", day11.generate_next_password("abcdefgh"))
        # self.assertEqual("ghjaabcc", day11.generate_next_password("ghijklmn"))

class Day11_IncrementStringTests(unittest.TestCase):
    
    def test_increment_string(self):
        self.assertEqual("abcxyzbc", day11.increment_string("abcxyzbb"))

    def test_increment_zzzzzzzz_wraps(self):
        self.assertEqual("aaaaaaaa", day11.increment_string("zzzzzzzz"))
    
    def test_increment_zzzzzzzz_wraps(self):
        self.assertEqual("aaaaaaaa", day11.increment_string("zzzzzzzz"))
        

class Day11_PasswordContainsStraight(unittest.TestCase):
    
    def test_contains_straight_at_beginning(self):
        self.assertTrue(day11.contains_straight("hijklmmn"))
        
    def test_contains_straight_at_end(self):
        self.assertTrue(day11.contains_straight("zzzabc"))
    
    def test_doesnt_contain_straight(self):
        self.assertFalse(day11.contains_straight("abbcegjk"))

class Day11_PasswordDoesntContainIOL(unittest.TestCase):
    
    def test_true(self):
        self.assertTrue(day11.contains_iol('foo'))
        self.assertTrue(day11.contains_iol('aaal'))
        self.assertTrue(day11.contains_iol('our'))
        
    def test_false(self):
        self.assertFalse(day11.contains_iol('abc'))
        self.assertFalse(day11.contains_iol('xyz'))

class Day11_ContainsTwoPairsTests(unittest.TestCase):
    
    def test_true(self):
        self.assertTrue(day11.contains_two_pairs('abbcdd'))
    
    def test_false(self):
        self.assertFalse(day11.contains_two_pairs('abbcded'))


import day12

class Day12_GetTotalTests(unittest.TestCase):
    
    def test_base(self):
        input_dict = {
            'a': [1, 2],
            'b': {'f': [3, 2, 1]},
            'c': {'d': 3, 'e': 2}
        }
        expect = 14
        actual = day12.get_total(input_dict)
        self.assertEqual(expect, actual)

import day13

class Day13_Tests(unittest.TestCase):
    
    def setUp(self):
        self.input_string = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

    def test_parse_input(self):
        result = day13.parse_input(self.input_string)
        self.assertEqual(-2, result['Alice']['David'])
        self.assertEqual(54, result['Alice']['Bob'])
        self.assertEqual(-63, result['Bob']['David'])
    
    def test_is_next_to(self):
        guest_order = ['Alice', 'Bob', 'Carol', 'David']
        self.assertTrue(day13.is_next_to('David', 'Alice', guest_order))
        self.assertTrue(day13.is_next_to('Alice', 'David', guest_order))
        self.assertFalse(day13.is_next_to('Bob', 'David', guest_order))
    
    def test_get_happiness_delta_for_person(self):
        example = """Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to Bob.
Carol would lose 62 happiness units by sitting next to Alice."""
        parsed = day13.parse_input(example)
        order = ['Alice', 'Bob', 'Carol']
        expect = -79 + -2
        self.assertEqual(expect, day13.get_happiness_delta_for_person('Alice', parsed, order))
    
    def test_generate_all_orders_of_guests(self):
        names = ['A', 'B']
        expect = [['A', 'B']] 
        result = day13.generate_all_orders_of_guests(names)
        self.assertEqual(expect, result)
        names = ['A', 'B', 'C']
        expect = [['A', 'B', 'C']] 
        result = day13.generate_all_orders_of_guests(names)
        self.assertEqual(expect, result)
        names = ['A', 'B', 'C', 'D']
        expect = [['A', 'B', 'C', 'D'], ['A', 'B', 'D', 'C'], ['A', 'C', 'B', 'D']]
        result = day13.generate_all_orders_of_guests(names)
        self.assertEqual(expect, result)

    def test_is_order_equivalent(self):
        self.assertTrue(day13.is_order_equivalent(['A', 'C', 'B', 'D'], ['B', 'C', 'A', 'D']))

    def test_input(self):
        graph = day13.parse_input(day13.INPUT_STRING)
        best = None
        for path in [p for p in day9.get_all_paths(graph) if all([loc in p for loc in graph.keys()])]:
            total = 0
            for person in path:
                h = day13.get_happiness_delta_for_person(person, graph, path)
                total += h
            if total > best:
                print total
                best = total
        print best

    def test_input_2(self):
        graph = day13.parse_input(day13.INPUT_STRING)
        names = graph.keys()
        graph['me'] = {}
        for n in names:
            graph['me'][n] = 0
            graph[n]['me'] = 0
        best = None
        for path in [p for p in day9.get_all_paths(graph) if all([loc in p for loc in graph.keys()])]:
            total = 0
            for person in path:
                h = day13.get_happiness_delta_for_person(person, graph, path)
                total += h
            if total > best:
                best = total
        print best

import day15
class Day15_Tests(unittest.TestCase):
    
    def test_test(self):
        test_input = day15.EXAMPLE_STRING

        ingredients = day15.get_ings_from_input(test_input)
        
        
        amounts = {'Butterscotch': 44, 'Cinnamon': 56}
        result = day15.calculate_total_score(amounts, ingredients)
        self.assertEqual(62842880, result)
        
        print day15.get_best_score(ingredients)
        
    def test_get_all_cookies(self):
        test_input = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
        ingredients = day15.get_ings_from_input(test_input)
        print ingredients
        
        result = day15.generate_all_cookies_with_max_size_n(ingredients, 3)
        result_list = [yielded for yielded in result]
        self.assertEqual(6, len(result_list))
    
    
        


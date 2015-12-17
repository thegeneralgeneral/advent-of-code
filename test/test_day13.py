import unittest
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
                best = total
        self.assertEqual(0, best)

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
        self.assertEqual(0, best)

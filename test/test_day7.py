import unittest

import day7

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

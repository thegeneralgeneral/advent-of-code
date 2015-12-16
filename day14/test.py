import unittest

import day14


class Day14_Tests(unittest.TestCase):
    
    def setUp(self):
        
        speed, duration, rest_time = 14, 10, 127
        self.comet = (speed, duration, rest_time)
        speed, duration, rest_time = 16, 11, 162
        self.dancer = (speed, duration, rest_time)
        
    
    def test_get_distance_travelled(self):
        t = 1  # seconds passed
        result = day14.get_distance_travelled(self.comet, t)
        self.assertEqual(14, result)
        result = day14.get_distance_travelled(self.dancer, t)
        self.assertEqual(16, result)
        
        t = 10  # seconds passed
        result = day14.get_distance_travelled(self.comet, t)
        self.assertEqual(140, result)
        result = day14.get_distance_travelled(self.dancer, t)
        self.assertEqual(160, result)
        
        t = 11  # seconds passed
        result = day14.get_distance_travelled(self.comet, t)
        self.assertEqual(140, result)
        result = day14.get_distance_travelled(self.dancer, t)
        self.assertEqual(176, result)
    
        t = 1000  # seconds passed
        result = day14.get_distance_travelled(self.comet, t)
        self.assertEqual(1120, result)
        result = day14.get_distance_travelled(self.dancer, t)
        self.assertEqual(1056, result)
    
    def test_input(self):
        import operator
        parsed = day14.parse_input(day14.INPUT_STRING)
        results = {}
        t = 2503
        for name, stats in parsed.iteritems():
            results[name] = day14.get_distance_travelled(stats, t)
        print results
        print sorted(results.items(), key=operator.itemgetter(1))
        
        points = day14.get_points(parsed, t)
        print sorted(points.items(), key=operator.itemgetter(1))
        
    def test_get_points(self):
        data = {'Comet': self.comet, 'Dancer': self.dancer}
        t = 1
        result = day14.get_points(data, t)
        expect = {'Dancer': 1}
        self.assertEqual(expect, result)
        
        t = 140
        result = day14.get_points(data, t)
        expect = {'Dancer': 139, 'Comet': 1}
        self.assertEqual(expect, result)
        
        t = 1000
        result = day14.get_points(data, t)
        expect = {'Dancer': 689, 'Comet': 312}
        self.assertEqual(expect, result)
    
    def test_get_points_2(self):
        data = {
            'A': (10, 1, 1),
            'B': (11, 1, 2)}
        for t in range(1, 5+1):
            result = day14.get_points(data, t)
            print result

import unittest
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

# import re
# import day15

# best_score = 0
# print 'starting'
# ings = day15.get_ings_from_input(day15.INPUT_STRING)
# print ings
# print day15.get_best_score_with_c_calories(ings, 500)
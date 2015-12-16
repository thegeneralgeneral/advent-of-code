
input_string = """
"""
import operator
import functools
import re

capacity = 100


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories
    
    def __repr__(self):
        return "%s: %s, %s, %s, %s, %s" % (self.name,
        self.capacity,
        self.durability,
        self.flavor,
        self.texture,
        self.calories)

def calculate_total_score(amount_dict, ingredients_dict):
    total = 0
    cap, dur, flv, tex = 0, 0, 0, 0
    total_calories = 0
    for name, n in amount_dict.iteritems():
        ing = ingredients_dict[name]
        cap += n * ing.capacity
        dur += n * ing.durability
        flv += n * ing.flavor
        tex += n * ing.texture
        total_calories += n * ing.calories
    total = max(cap, 0) * max(dur, 0) * max(flv, 0) * max(tex, 0)
    return total, total_calories

def get_ings_from_input(input_string):
    ingredients = {}
    for line in input_string.split('\n'):
        regex = r'([A-z]+): capacity ([-\d]+), durability ([-\d]+), flavor ([-\d+]+), texture ([\-\d]+), calories ([\-\d]+)'
        match = re.search(regex, line)
        name, capacity, durability, flavor, texture, calories = tuple([match.group(1)] + [int(i) for i in [match.group(2), match.group(3), match.group(4), match.group(5), match.group(6)]])
        i = Ingredient(name, capacity, durability, flavor, texture, calories)
        ingredients[name] = i
    return ingredients

def generate_all_cookies_with_max_size_n(ingredients, n):
    amounts = {}
    if not ingredients:
        yield amounts
    elif len(ingredients) == 1:
        yield {ingredients.keys()[0]: n}
    else:
        for name, ing in ingredients.iteritems():
            # Try 0-100 of each of the ingredients, recurse on 100-n
            for i in range(n):
                # Get all of the subcombinations for the remaining amount (n - i) and ingredients
                remaining_ingredients = ingredients.copy()
                remaining_ingredients.pop(ing.name, None)
                for subcomb in generate_all_cookies_with_max_size_n(remaining_ingredients, n-i):
                    # Add ing[name]: i
                    # Update with all subcombinations and yield them all
                    result = subcomb.copy()
                    result.update({ing.name: i})
                    yield result
                
def get_best_score(ings):
    best_score = 0
    for combo in generate_all_cookies_with_max_size_n(ings, 100):
        score = calculate_total_score(combo, ings)
        if score > best_score:
            print '%s -- %s' % (score, combo)
            best_score = score
    return best_score

def get_best_score_with_c_calories(ings, c):
    best_score = 0
    for combo in generate_all_cookies_with_max_size_n(ings, 100):
        score, calories = calculate_total_score(combo, ings)
        if calories != c:
            continue
        if score > best_score:
            print '%s -- %s' % (score, combo)
            best_score = score
    return best_score

EXAMPLE_STRING =  """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

INPUT_STRING = """Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8"""
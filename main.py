# Day 1
# import day1
# print day1.calculate_floor(day1.INPUT_STRING)
# print day1.calculate_basement_step(day1.INPUT_STRING)

# Day 2
# import day2
# inputs = day2.INPUT_STRING.split()
# lwh_tuples = [tuple([int(n) for n in l.split('x')]) for l in inputs]
# total = sum([day2.get_paper_area(l, w, h) for l, w, h in lwh_tuples])
# print total

# print day2.get_ribbon_length(2, 3, 4)
# print day2.get_ribbon_length(1, 1, 10)

# total = sum([day2.get_ribbon_length(l, w, h) for l, w, h in lwh_tuples])
# print total

# Day 3
import day3
print day3.get_num_houses_visited(day3.INPUT_STRING)
print day3.get_total_houses_visited_with_robo_santa(day3.INPUT_STRING)
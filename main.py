# Day 1
# import day1
# print day1.calculate_floor(day1.INPUT_STRING)
# print day1.calculate_basement_step(day1.INPUT_STRING)

# Day 2
import day2
inputs = day2.INPUT_STRING.split()
lwh_tuples = [tuple([int(n) for n in l.split('x')]) for l in inputs]
total = sum([day2.get_paper_area(l, w, h) for l, w, h in lwh_tuples])
print total

# print day2.get_ribbon_length(2, 3, 4)
# print day2.get_ribbon_length(1, 1, 10)

# total = sum([day2.get_ribbon_length(l, w, h) for l, w, h in lwh_tuples])
# print total

# Day 3
# import day3
# print day3.get_num_houses_visited(day3.INPUT_STRING)
# print day3.get_total_houses_visited_with_robo_santa(day3.INPUT_STRING)

# import day4
# result = day4.get_suffix_num_resulting_in_five_zeroes("iwrupvqb")
# print result
# result = day4.get_suffix_num_resulting_in_six_zeroes("iwrupvqb")
# print result

# import day5
# inputs = day5.INPUT_STRING.split('\n')
# num_nice = 0
# for i in inputs:
#     if day5.is_nice(i):
#         num_nice += 1
# print "Num nice: %s" % num_nice

# num_nice = 0
# for s in inputs:
#     if day5.is_nice_2(s):
#         num_nice += 1
# print "Num nice 2: %s" % num_nice  # 203 is too high

# import day6
# grid = day6.get_1000_by_1000_grid()
# for i in day6.INPUT_STRING.split('\n'):
#     grid = day6.apply_instruction_string_to_grid(i, grid)
# print day6.get_brightness(grid)

# import day7
# import datetime

# print 'started: %s' % datetime.datetime.utcnow()
# circuit = day7.Circuit(day7.INPUT_STRING)
# print circuit.resolve_value('a')
# print 'stopped part 1: %s' % datetime.datetime.utcnow()

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

# Day 9
# result = my_func(day9.INPUT_STRING)
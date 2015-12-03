# Day 1
# import day1
# print day1.calculate_floor(day1.INPUT_STRING)
# print day1.calculate_basement_step(day1.INPUT_STRING)

# Day 2

inputs = day2.INPUT_STRING.split()
print len(inputs)
lwh_tuples = [tuple(l.split('x')) for l in inputs]
total = sum([day2.get_paper_area(int(l), int(w), int(h)) for l, w, h in lwh_tuples])
print total
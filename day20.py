
from __future__ import print_function
import numpy as np

BIG_NUM = 1000000  # try larger numbers until solution found

goal = 34000000
houses_a = np.zeros(BIG_NUM)
houses_b = np.zeros(BIG_NUM)

for elf in xrange(1, BIG_NUM):
    houses_a[elf::elf] += 10 * elf
    houses_b[elf:(elf+1)*50:elf] += 11 * elf

print(np.nonzero(houses_a >= goal)[0][0])
print(np.nonzero(houses_b >= goal)[0][0])


# def get_presents_by_elf_for_house(elf, house):
#     if house % elf == 0:
#         return 10 * elf
#     return 0

# def get_num_presents(house):
#     # The highest # elf that will affect this house is the house #.
#     total = 0
#     for elf in range(1, house+1):
#         num = get_presents_by_elf_for_house(house+1-elf, house)
#         # print 'Adding presents from elf %s (%s)' % (house+1-elf, num)
#         total += num
#         if total > 34000000:
#             print 'FOUND: %s' % house
#         # if elf > 50:
#         #     break
#     return total

# def get_first_house_with_n_presents(n, start=1):
#     for i in range(n):
#         for elf in range(n):
#             pass

# #######

def get_presents_by_elf_for_house(elf, house):
    if house % elf == 0:
        return 10 * elf
    return 0

def get_num_presents(house):
    # The highest # elf that will affect this house is the house #.
    total = 0
    for elf in range(1, house+1):
        num = get_presents_by_elf_for_house(house+1-elf, house)
        # print 'Adding presents from elf %s (%s)' % (house+1-elf, num)
        total += num
        if total > 34000000:
            print 'FOUND: %s' % house
        # if elf > 50:
        #     break
    return total

def get_first_house_with_n_presents(n, start=1, limit=10000000):
    for i in range(start, limit,  1):
        num = get_num_presents(i)
        if i % 1000 == 0:
            print '%s: %s' % (i, num)
        # print 'House %s gets %s presents.' % (i, num)
        if num >= n:
            print 'FOUND: %s (%s)' % (i, num)
            return i
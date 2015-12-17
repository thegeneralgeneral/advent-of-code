
def get_all_combinations(container_size_list, amount):
    if amount == 0 or not container_size_list:
        pass
    else:
        if container_size_list[0] == amount:
            yield [container_size_list[0]]
        # Get the remaining valid combinations if we use this container
        first_container = container_size_list[0]
        for valid_subcomb in get_all_combinations(container_size_list[1:], amount - first_container):
            yield [first_container] + valid_subcomb
        # Get the valid combinations if we *don't* use this container.
        for valid_subcomb in get_all_combinations(container_size_list[1:], amount):
            yield valid_subcomb

def get_all_combinations_of_min_length(container_size_list, amount):
    min_length = 9999999
    acceptable_results = []
    for combo in get_all_combinations(container_size_list, amount):
        # If this combo is smaller in length than any we've seen so far, scrap the existing list and start with this one
        # If this combo is the same length as the minimum, add it to the list.
        # Otherwise, continue.
        if len(combo) < min_length:
            acceptable_results = [combo]
            min_length = len(combo)
        elif len(combo) == min_length:
            acceptable_results.append(combo)
        else:
            continue
    return acceptable_results

PUZZLE_CONTAINERS = [int(i) for i in """50
44
11
49
42
46
18
32
26
40
21
7
18
43
10
47
36
24
22
40""".split('\n')]
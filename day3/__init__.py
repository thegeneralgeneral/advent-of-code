X = 0
Y = 1

def get_num_houses_visited(input_string):
    position = [0, 0]
    houses_visited = [[position[X], position[Y]]]
    print "Initial houses visited: %s" % houses_visited
    for c in input_string:
        if c == '^':
            position[Y] -= 1
        elif c == 'v':
            position[Y] += 1
        elif c == '<':
            position[X] -= 1
        elif c == '>':
            position[X] += 1
        print "Position: %s" % position
        print position in houses_visited
        if position not in houses_visited:
            print "New position detected."
            houses_visited.append(position)
        print houses_visited
        
    return len(houses_visited)


def get_distance_travelled(reindeer, t):
    speed, duration, rest = reindeer
    total_cycle_length = duration + rest
    cycles_completed = t / total_cycle_length
    total_distance = 0
    total_distance += cycles_completed * (speed * duration)

    remaining_seconds = t - (cycles_completed * total_cycle_length)
    # up to <duration> of the remaining seconds count towards the total
    remaining_useful_seconds = min([remaining_seconds, duration])
    total_distance += speed * remaining_useful_seconds
    return total_distance


import operator
import time
def get_points(data, t):
    # a point is awarded to the reindeer in the lead each second
    points = {}
    for s in range(1, t+1):
        print '--- Second %s ---' % s
        current_status = {}
        for name in data.keys():
            current_status[name] = get_distance_travelled(data[name], s)
        print current_status
        sorted_distances = sorted(current_status.items(), key=operator.itemgetter(1))
        print sorted_distances
        winning_distance = sorted_distances[-1][1]
        winning_names = [key for key,value in current_status.items() if value == winning_distance]
        print 'Winner: %s' % winning_names
        for name in winning_names:
            if not points.get(name):
                points[name] = 1
            else:
                points[name] += 1
        print 'Points: %s' % points
        #time.sleep(3)
    return points
    

import re
def parse_input(input_string):
    result = {}
    regex = r'([A-z]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
    for line in input_string.split('\n'):
        print line
        match = re.match(regex, line)
        print match.group(0)
        print match.group(1)
        print match.group(2)
        print match.group(3)
        print match.group(4)
        result[match.group(1)] = (int(match.group(2)),
                                  int(match.group(3)),
                                  int(match.group(4)))
    return result

INPUT_STRING = """Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds."""
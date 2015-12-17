import re

def map_distances(input_string):
    format_regex = r'([A-Za-z]+) to ([A-Za-z]+) = (\d+)'
    parsed_input = [(match.group(1), match.group(2), int(match.group(3))) for match in [re.match(format_regex, line) for line in input_string.split('\n')]]
    
    dist_map = {}
    for source, dest, dist in parsed_input:
        # A to B
        dist_map[source] = dist_map.get(source) or {}
        dist_map[source][dest] = dist
        # B to A
        dist_map[dest] = dist_map.get(dest) or {}
        dist_map[dest][source] = dist
    return dist_map

def get_all_paths_from_a_to_b(a, b, graph, exclude_nodes=[]):
    # A path is a list of locations. The actual distance can be looked up from the graph.
    options_from_a = [name for name in graph[a].keys() if not name in exclude_nodes]
    paths = []
    for next_location in options_from_a:
        # Base case: next_location *is* b; don't need to recurse.
        if next_location == b:
            paths.append([a, b])
        else:
            exclude_nodes = exclude_nodes + [a]
            paths_from_next_location_to_b = get_all_paths_from_a_to_b(next_location, b, graph, exclude_nodes)
            [paths.append([a] + remaining_path) for remaining_path in paths_from_next_location_to_b]
    return paths

def get_all_paths(graph):
    paths = []
    for source in graph.keys():
        for dest in [loc for loc in graph.keys() if loc != source]:
            paths.extend(get_all_paths_from_a_to_b(source, dest, graph))
    return paths

def get_length_of_path(path, graph):
    if len(path) == 2:
        return graph[path[0]][path[1]]
    else:
        return graph[path[0]][path[1]] + get_length_of_path(path[1:], graph)

def get_shortest_complete_path(graph):
    shortest_dist = 999999999
    shortest_path = None
    for path in [p for p in get_all_paths(graph) if all([loc in p for loc in graph.keys()])]:
        length = get_length_of_path(path, graph)
        if length < shortest_dist:
            shortest_dist = length
            shortest_path = path
    return shortest_path, shortest_dist

def get_longest_complete_path(graph):
    longest_dist = 0
    longest_path = None
    for path in [p for p in get_all_paths(graph) if all([loc in p for loc in graph.keys()])]:
        length = get_length_of_path(path, graph)
        if length > longest_dist:
            longest_dist = length
            longest_path = path
    return longest_path, longest_dist

INPUT_STRING = """AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90"""

# TODO - alternate approach: just keep list of "on" nodes/lights

#####
### Below is copied from a code kata I did a while back ;)
#####

DEAD, ALIVE = 0, 1

def generate_next_cell_state(current_state, num_alive_neighbours):
    if current_state == ALIVE:
        if 2 <= num_alive_neighbours <= 3:
            return ALIVE
    elif num_alive_neighbours == 3:
        return ALIVE
    return DEAD

def count_alive_neighbours(grid, x, y):
    total = 0
    height = len(grid)
    width = len(grid[0])

    # previous row
    # current row (minus self)
    # next row

    total += grid[y-1][x-1] + grid[y-1][x] + grid[y-1][(x+1) % width]
    print "%s total after first row" % total
    total += grid[y][x-1] + grid[y][(x+1) % width]
    print "%s total after 2nd row" % total
    total += grid[(y+1)%height][x-1] + grid[(y+1)%height][x] + grid[(y+1)%height][(x+1) % width]
    print "%s total after 3rd row" % total
    return total

def generate_next_state(state):
    width = len(state[0])
    height = len(state)
    result = []
    for y in range(height):
        row = []
        for x in range(width):
            num_alive_neighbours = count_alive_neighbours(state, x, y)
            cell_state = generate_next_cell_state(state[y][x], num_alive_neighbours)
            row.append(cell_state)
        result.append(row)
    return result

#############################################################################################

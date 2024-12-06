import copy
import time

def read_maze(filename: str) -> str:
    return open(filename).read()



def is_obstacle(maze: list, x: int, y: int, direction) -> bool:
    if direction == "^":
        return maze[x-1][y] == "#"
    elif direction == ">":
        return maze[x][y+1] == "#"
    elif direction == "v":
        return maze[x+1][y] == "#"
    else:
        return maze[x][y-1] == "#"

def move(x: int, y: int, direction: str) -> tuple:
    if direction == "^":
        return x-1, y
    elif direction == ">":
        return x, y+1
    elif direction == "v":
        return x+1, y
    else:
        return x, y-1

def turn_90(direction: str):
    if direction =='>':
        return 'v'
    elif direction =='v':
        return '<'
    elif direction =='<':
        return '^'
    else:
        return '>'

def find_guard_path_v2(maze: list, start_x: int, start_y: int, direction: str):
    total_distinct_positions = set()

    x, y = start_x, start_y
    cycle = False
    visited_obstacle = set()

    total_distinct_positions.add((x,y))
    while x<len(maze)-1 and y<len(maze[0])-1 and (x>0 and y>0) and not cycle:

        while is_obstacle(maze, x, y, direction):
            if (x,y,direction) in visited_obstacle:
                cycle = True
                break
            visited_obstacle.add((x,y,direction))
            direction = turn_90(direction)
        if not cycle:
            x, y = move(x, y, direction)
            #print_maze(maze, x, y, direction)
            total_distinct_positions.add((x,y))
    return total_distinct_positions, cycle
        
def cycles(maze: list, start_x: int, start_y: int, start_direction: str, positions: set):
    total_cycles = 0
    for pos_x, pos_y in positions:

        new_maze = copy.deepcopy(maze)
        new_maze[pos_x][pos_y] = "#"

        _, cycle = find_guard_path_v2(new_maze, start_x, start_y, start_direction)

        total_cycles += cycle
    return total_cycles
        
        
    

def find_start_position(maze: list) -> tuple:

    for i, _ in enumerate(maze):
        for j,_ in enumerate(maze[i]):
            if maze[i][j] == "^":
                return i,j,"^"
            elif maze[i][j] == ">":
                return i,j,">"
            elif maze[i][j] == "v":
                return i,j,"v"
            elif maze[i][j] == "<":
                return i,j,"<"
    return -1

def print_maze(maze_print: list, x: int, y: int, direction: str, cycles: int = 0) -> None:
    maze_print[x][y] = direction
    print('*'*100)
    print(f"Cycle {cycles} in {x}, {y}")
    for row in maze_print:
        print("".join(row))
    print('*'*100)
    maze_print[x][y] = "."

def print_positions(maze_print,positions: list) -> None:
    for x,y in positions:
        maze_print[x][y] = "X"
    for row in maze_print:
        print("".join(row))
    

def part1(filename: str) -> int:
    maze = read_maze(filename).split("\n")
    maze = [[c for c in row] for row in maze]


    start_x, start_y, start_direction = find_start_position(maze)

    total_distinct_positions, _ = find_guard_path_v2(maze, start_x, start_y, start_direction)
    return len(total_distinct_positions) 

def part2(filename: str) -> int:
    maze = read_maze(filename).split("\n")
    maze = [[c for c in row] for row in maze]

    start_x, start_y, start_direction = find_start_position(maze)
    total_distinct_positions, _  = find_guard_path_v2(maze, start_x, start_y, start_direction)
    return cycles(maze, start_x, start_y, start_direction, total_distinct_positions)
   
        

if __name__ == "__main__":
    print("Solution for Part 1 is", part1('data/input6.txt'))
    print("Solution for Part 2 is", part2('data/input6.txt'))
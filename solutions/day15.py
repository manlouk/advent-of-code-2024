DIRECTION = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1)
}

def is_valid_move(position: tuple, move: str, warehouse_map: list):
    
    position = (position[0] + DIRECTION[move][0], position[1] + DIRECTION[move][1])
    
    symbol = warehouse_map[position[1]][position[0]]

    if warehouse_map[position[1]][position[0]] == '.':
        return True
    
    if warehouse_map[position[1]][position[0]] == '#':
        return False
    
    if move in ['^','v']:
        if symbol== '[':
            return is_valid_move(position, move, warehouse_map) and is_valid_move((position[0]+1, position[1]), move, warehouse_map)
        elif symbol == ']':
            return is_valid_move(position, move, warehouse_map) and is_valid_move((position[0]-1, position[1]), move, warehouse_map)
        else:
            return is_valid_move(position, move, warehouse_map)
    else:
        return is_valid_move(position, move, warehouse_map)

def backtrack(position: tuple, move: str, warehouse_map: list, symbol: str):
    """Predicts the motion of the robot and boxes in the expanded warehouse."""

   
    new_position = (position[0] + DIRECTION[move][0], position[1] + DIRECTION[move][1])
    if not is_valid_move(position, move, warehouse_map):
        return position
    
    if is_valid_move(position, move, warehouse_map) and warehouse_map[new_position[1]][new_position[0]] == '.':
        warehouse_map[position[1]][position[0]] = '.'
        warehouse_map[new_position[1]][new_position[0]] = symbol
        return new_position
    if is_valid_move(position, move, warehouse_map):
        backtrack(new_position, move, warehouse_map, warehouse_map[new_position[1]][new_position[0]])
        warehouse_map[position[1]][position[0]] = '.'
        warehouse_map[new_position[1]][new_position[0]] = symbol

    return new_position


def backtrack_double(position: tuple, move: str, warehouse_map: list, symbol: str):
    """Predicts the motion of the robot and boxes in the expanded warehouse."""

   
    new_position = (position[0] + DIRECTION[move][0], position[1] + DIRECTION[move][1])
    if not is_valid_move(position, move, warehouse_map):
        return position
    
    if is_valid_move(position, move, warehouse_map) and warehouse_map[new_position[1]][new_position[0]] == '.':
    
        warehouse_map[position[1]][position[0]] = '.'
        warehouse_map[new_position[1]][new_position[0]] = symbol       
        return new_position
            
       
    if is_valid_move(position, move, warehouse_map):
            
        if move in ['^','v']: 
            if warehouse_map[new_position[1]][new_position[0]] =='[':
                backtrack_double((new_position[0]+1, new_position[1]), move, warehouse_map, warehouse_map[new_position[1]][new_position[0]+1])
               
            if warehouse_map[new_position[1]][new_position[0]] ==']':
                backtrack_double((new_position[0]-1, new_position[1]), move, warehouse_map, warehouse_map[new_position[1]][new_position[0]-1])
               
 
        backtrack_double(new_position, move, warehouse_map, warehouse_map[new_position[1]][new_position[0]])
    
        warehouse_map[position[1]][position[0]] = '.'
        warehouse_map[new_position[1]][new_position[0]] = symbol
       
    return new_position


def warehouse_plot(warehouse_map_2: list):
    for line in warehouse_map_2:
        print("".join(line))
    print()

with open('data/input15.txt') as f:
    warehouse, moves = f.read().strip().split('\n\n')
    warehouse_map = [[x for x in line] for line in warehouse.strip().split('\n')]
    moves = [x for move in moves.split('\n') for x in move]

    MAX_X = len(warehouse_map[0])
    MAX_Y = len(warehouse_map)

    for i in range(MAX_Y):
        for j in range(MAX_X):
            if warehouse_map[i][j] =='@':
                robot_start_position = (j,i)
                break
    
    robot_position = robot_start_position
    
    for move in moves:
        robot_position = backtrack(robot_position, move, warehouse_map, '@')

    total = 0
    for i in range(MAX_Y):
        for j in range(MAX_X):
            if warehouse_map[i][j] == 'O':
                total += 100*i + j
    print(total)



with open('data/input15.txt') as f:
    warehouse, moves = f.read().strip().split('\n\n')
    warehouse_map = [[x for x in line] for line in warehouse.strip().split('\n')]
    moves = [x for move in moves.split('\n') for x in move]

    MAX_X = len(warehouse_map[0])
    MAX_Y = len(warehouse_map) 

    double_warehouse_map = []
    for i in range(MAX_Y):
        line = []
        for j in range(MAX_X):
            if warehouse_map[i][j]=='@':
                line.extend(['@','.'])
            elif warehouse_map[i][j]=='O':
                line.extend(['[',']'])
            else:
                line.extend([warehouse_map[i][j],warehouse_map[i][j]])
        double_warehouse_map.append(line)

    MAX_X = len(double_warehouse_map[0])
    MAX_Y = len(double_warehouse_map)

    for i in range(MAX_Y):
        for j in range(MAX_X):
            if double_warehouse_map[i][j] =='@':
                robot_start_position = (j,i)
                break
    
    robot_position = robot_start_position

    for move in moves:
        new_robot_position = backtrack_double(robot_position, move, double_warehouse_map, '@')
        print(f"Move: {move}")
        robot_position = new_robot_position

    warehouse_plot(double_warehouse_map)
    
    total = 0
    for i in range(MAX_Y):
        for j in range(MAX_X):
            if double_warehouse_map[i][j] == '[':
                total += 100*i + j
    print(total)
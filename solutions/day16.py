import heapq

# Classic dijkstra problem


DIRECTIONS = {
    (0,1,'>'),
    (1,0,'v'),
    (-1,0,'^'),
    (0,-1,'<')
}

def get_adjacent_nodes(v,max_x, max_y, maze, visited):
    neighbors = []
    for direction in DIRECTIONS:
        if v[0]+direction[0]<max_y and v[1]+direction[1]<max_x and v[0]+direction[0]>=0 and v[1]+direction[1]>=0:
            if maze[v[0]+direction[0]][v[1]+direction[1]]!='#' and (v[0]+direction[0], v[1]+direction[1],direction[2]) not in visited:
                neighbors.append((v[0]+direction[0], v[1]+direction[1],direction[2]))
    return neighbors


def plot_maze(maze: list):
    for line in maze:
        print(''.join(line))
    
def dfs(node, end_point, visited, max_x, max_y, tiles):
    
    if (node[0],node[1]) ==end_point and dist[node]==sol1:
        return [tiles]

    
    paths = []
    for neighbor in get_adjacent_nodes(node, max_x, max_y, maze, visited):
        weight = 1
        if neighbor[2]!=node[2]:
            weight = 1001

        if dist[neighbor] == dist[node]+weight:
            path = dfs(neighbor, end_point, visited, max_x, max_y, tiles+[neighbor])
            if path:
                paths.extend(path)

    return paths


with open('data/input16.txt','r') as f:
    maze = []
    for line in f:
        maze.append([c for c in line.strip()])

    MAX_X = len(maze[0])
    MAX_Y = len(maze)
    
    start_point = None
    end_point = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]=='S':
                start_point = (i,j,'>')
            if maze[i][j]=='E':
                end_point = (i,j)


    pq = []
    dist  = {}
    for i in range(MAX_Y):
        for j in range(MAX_X):
            dist[(i,j,'>')] = float('inf')
            dist[(i,j,'<')] = float('inf')
            dist[(i,j,'v')] = float('inf')
            dist[(i,j,'^')] = float('inf')
    
    dist[start_point] = 0
    visited = set()
    visited.add((start_point[0], start_point[1]))

    heapq.heappush(pq, (0,start_point))

    direction = {}
    direction[(start_point[0],start_point[1])]='>'

    parent = {start_point:start_point}

    while pq:
        d, u = heapq.heappop(pq)
        

        visited.add((u[0],u[1],u[2]))
        for neighbor in get_adjacent_nodes(u, MAX_X, MAX_Y, maze, visited):
            weight = 1
            
            if u[2]!=neighbor[2]:
                weight += 1000


            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor],neighbor))

    sol1 = float('inf')   
    for x in dist:
        if x[0]==end_point[0] and x[1]==end_point[1]:
            if dist[x]<sol1:
                sol1 = dist[x]
    print(sol1)


    # Part 2
    visited  = set((start_point))

    optimal_routes = dfs(start_point,end_point,visited, max_x=MAX_X, max_y=MAX_Y, tiles = [start_point])


    optimal_tiles = set()
    for route in optimal_routes:
        for tile in route:
            optimal_tiles.add((tile[0],tile[1]))

    sol2 = len(optimal_tiles)
    print(sol2)
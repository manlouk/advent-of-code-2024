from collections import deque

def get_neighbors(v, max_x, max_y):

    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    neighbors = []

    for direction in directions:
        if v[0]+direction[0] <=max_x and v[1]+direction[1]<=max_y and v[0]+direction[0]>=0 and v[1]+direction[1]>=0:
            neighbors.append((v[0]+direction[0],v[1]+direction[1]))
    return neighbors
    
    

with open('data/input18.txt','r') as f:
    lines = f.readlines()
    
    bytes = [[int(a) for a in x.strip().split(',')] for x in lines ][:1024]


    fallen_bytes = set()
    for byte in bytes:
        fallen_bytes.add(tuple(byte))



    max_x = 6
    max_y = 6

    s = (0,0)
    visited = set()
    parent = {}

    q = deque()
    q.append(s)
    visited.add(s)

    parent[s] = s

    while len(q):
        v = q.popleft()
        for neighbor in get_neighbors(v, max_x, max_y):
            if neighbor not in visited:
                parent[neighbor] = v
                visited.add(neighbor)
                if neighbor not in fallen_bytes:
                    q.append(neighbor)
    
    # path = []
    # current_node = (2,2)
    # while current_node!= (0,0):
    #     path.append(current_node)
    #     current_node = parent[current_node]

    # sol1 = len(path)
    # print(path)
    # print(sol1)


    #Part 2
    bytes = [[int(a) for a in x.strip().split(',')] for x in lines ][1024:]
    sol2 = None
    for byte in bytes:
        parent = {}
        fallen_bytes.add(tuple(byte))
        max_x = 70
        max_y = 70

        s = (0,0)
        visited = set()

        q = deque()
        q.append(s)
        visited.add(s)


        while len(q):
            v = q.popleft()
            for neighbor in get_neighbors(v, max_x, max_y):
                if neighbor not in visited:
                    parent[neighbor] = v
                    visited.add(neighbor)
                    if neighbor not in fallen_bytes:
                        q.append(neighbor)
        


        
        if (70,70) not in parent:
            sol2 = byte
            break
            


    print(sol2)



   
            
            

        

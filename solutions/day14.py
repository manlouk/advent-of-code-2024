
import copy
import numpy as np

def move(p,v, max_x, max_y):

    
    p[0]  = (p[0]+v[0])%max_x
    p[1]  = (p[1]+v[1])%max_y
    
    return p
    

input = open('data/input14.txt').read().strip().split("\n")
q1 = 0
q2 = 0
q3 = 0
q4 = 0

MAX_X = 101
MAX_Y = 103

for robot in input:
    p, v = [x.replace('p=','').replace('v=','').split(',') for x in robot.split(' ')]   
    p = [int(x) for x in p]
    v = [int(x) for x in v]

    for _ in range(100):
        p = move(p,v, MAX_X, MAX_Y)

    if p[0]<MAX_X//2 and p[1]<MAX_Y//2:
        q1+=1
    elif p[0]>MAX_X//2 and p[1]<MAX_Y//2:
        q2+=1
    elif p[0]<MAX_X//2 and p[1]>MAX_Y//2:
        q3+=1
    else:
        if p[0]>MAX_X//2 and p[1]>MAX_Y//2:
            q4+=1

sol1 = q1*q2*q3*q4
print(sol1)

#Part 2
def print_tiles(positions, max_x, max_y):
    tiles = [['.' for _ in range(max_x)] for _ in range(max_y)]
    print(tiles)
  
    for p in positions:
        tiles[p[0][1]][p[0][0]] = '#'
    for line in tiles:
        print("".join(line))
    print()

MAX_X = 101
MAX_Y = 103

robots_positions = []
for robot in input:

    p, v = [x.replace('p=','').replace('v=','').split(',') for x in robot.split(' ')]   
    p = [int(x) for x in p]
    v = [int(x) for x in v]
    robots_positions.append((p,v))


min_std = 10000000
christmas_tree = []
iteration = 0

q1 = []
q2 = []
q3 = []
q4 = []
for i in range(MAX_X*MAX_Y):
    new_positions = []

    for pos,v in robots_positions:

        new_pos = move(pos,v, MAX_X, MAX_Y)
        new_positions.append((new_pos,v))
    
    robots_positions = new_positions

    stdev1 = np.std([p[0] for p,_ in robots_positions])
    stdev2 = np.std([p[1] for p,_ in robots_positions])
    std = stdev1 + stdev2
    if std < min_std:
        min_std = std
        christmas_tree = copy.deepcopy(new_positions)
        iteration = i
   

print_tiles(christmas_tree, MAX_X, MAX_Y)





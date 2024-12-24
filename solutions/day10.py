import time 
import copy
def read_input(filename: str) -> list:
    with open(filename, 'r') as f:
        input = f.read().strip().split("\n")
        parsed_input = []
        for line in input:
            line = [int(x) for x in line]
            parsed_input.append(line)
    return parsed_input


def is_trail(route: list) -> bool:

    for i in range(0,len(route)):
       if route[i]!=i:
           return False
    return True

# def print_route(input: list, x,y):
#     input_copy = copy.deepcopy(input)
#     input_copy[x][y] = "X"
#     for line in input_copy:
#         print("".join([str(x) for x in line]))
#     print()

def valid_trail(trail: list) -> bool:
    return trail[-1] in [(trail[-2][0]+1,trail[-2][1]),(trail[-2][0]-1,trail[-2][1]),(trail[-2][0],trail[-2][1]+1),(trail[-2][0],trail[-2][1]-1)]

def print_trail(input,trail: list):
    input_copy = copy.deepcopy(input)
    for x,y in trail:
        input_copy[x][y] = f"[{input_copy[x][y]}]"
    for line in input_copy:
        print("".join([str(x) for x in line]))
    print()    



def find_trailheads(input: list) -> list:
    
    visited = set()
    ends = set()
    def traihead_score(i,j,route, trail):
        
       
        visited.add((i,j))
       
        score = 0

        if not is_trail(route):
            return 0
        if len(route)>10:
           
            return 0
        if is_trail(route) and len(route)==10 and valid_trail(trail):
        #and (trail[0][0],trail[0][1],trail[-1][0],trail[-1][1]) not in ends:
            #ends.add((trail[0][0],trail[0][1],trail[-1][0],trail[-1][1]))
            return 1
        
    
        for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0<=x<len(input) and 0<=y<len(input[0]):
                if (x,y) in visited:
                    continue
                score+=traihead_score(x, y, route + [input[x][y]], trail+[(x,y)])

                visited.remove((x,y))
        
        return score

    total_score = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 0:
                total_score += traihead_score(i, j,[0], [(i,j)])
    return total_score
    
    
input = read_input("data/input10.txt")

print(find_trailheads(input))


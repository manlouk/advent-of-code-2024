
# from collections import Counter
# def read_input(filename: str) -> list:
#     with open(filename, 'r') as input:
#         return [ [c for c in line] for line in  input.read().strip().split('\n')]

# grid = read_input('data/input12.txt')

# x_range = len(grid)
# y_range = len(grid[0]) 





# def build_graph(grid):
#     graph = []
#     for i in range(x_range):
#         for j in range(y_range):
#             if i+1 < x_range:
#                 graph.append([(i,j),(i+1,j)])
#             if j+1 < y_range:
#                 graph.append([(i,j),(i,j+1)])
#             if i-1 >= 0:
#                 graph.append([(i,j),(i-1,j)])
#             if j-1 >= 0:
#                 graph.append([(i,j),(i,j-1)])

#     return graph


# graph = build_graph(grid)


# parent = {(i,j): (i,j) for i in range(x_range) for j in range(y_range)}
# rank = {(i,j): 0 for i in range(x_range) for j in range(y_range)}

# side_x = {}


# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]

# def union(x: tuple,y: tuple):


#     x_repr = find(x)
#     y_repr = find(y)

#     if x_repr == y_repr:
#         return 
    
#     if rank[x_repr] < rank[y_repr]:

#         parent[x_repr] = y_repr
        
#     elif rank[x_repr] > rank[y_repr]:
#         parent[y_repr] = x_repr

#     else:
#         parent[y_repr] = x_repr
#         rank[x_repr] +=1


# for edge in graph:
#     if grid[edge[0][0]][edge[0][1]] == grid[edge[1][0]][edge[1][1]]:
#         union(edge[0],edge[1])
   

# groups = {}
# for k in parent:
#     root = find(k)  # Ensure path compression is applied for all nodes
#     if root not in groups:
#         groups[root] = []
#     groups[root].append(k)


   
# total_perimeter = {group: 4*len(groups[group]) for group in groups}


# for group in groups:
#     for (i,j) in groups[group]:
       
#         if (i,j+1) in groups[group]:
               
#             total_perimeter[group] -=1
               
 
#         if  (i,j-1) in groups[group]:
               
          
#             total_perimeter[group] -=1
                
#         if  (i+1,j) in groups[group]:
        
           
#             total_perimeter[group] -=1
        
               
#         if (i-1,j) in groups[group]:
#             total_perimeter[group] -=1

# total_sides = {group: 4 for group in groups}

# for group in groups:
#     groups[group] = sorted(groups[group], key=lambda x: x[0])
#     missing_sides = set()
#     min_x = min([i for i,_ in groups[group]])
#     max_x = max([i for i,_ in groups[group]])
#     min_y = min([j for _,j in groups[group]])
#     max_y = max([j for _,j in groups[group]])
#     for (i,j) in groups[group]:
       
#         if (i,j+1) not in groups[group] and j+1<=max_y:
#             missing_sides.add((i,j+1))
#         if  (i,j-1) not in groups[group] and j-1>=min_y:
#             missing_sides.add((i,j-1))   
#         if  (i+1,j) not in groups[group] and i+1<=max_x:
#             missing_sides.add((i+1,j)) 
#         if (i-1,j) not in groups[group] and i-1>=min_x:
#             missing_sides.add((i-1,j))

#     xs = Counter([x for x,_ in missing_sides])
#     ys = Counter([y for _,y in missing_sides])
#     lines = len([x for x in xs if xs[x]>=1]) + len([y for y in ys if ys[y]>=1])
#     lines += 4*len([x for x in xs if xs[x]==1]) + 4*len([y for y in ys if ys[y]==1])

#     print(xs)
#     print(ys)

#     print(missing_sides)

#     total_sides[group] += lines

#     print(lines)




        


# for group in groups:
#     print(f"Group {grid[group[0]][group[1]]}: {total_sides[group]}")

# cost = sum([total_sides[group] *len(groups[group])  for group in groups])
# print(cost)      
# # cost = sum([perimeter * len(groups[group])  for group, perimeter in total_perimeter.items()])
# # print(f"Cost with perimeter: {cost}")


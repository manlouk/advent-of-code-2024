import os


def is_chief_historian_lan(cycle: set):
    
    return 't' in [cycle[0][0],cycle[1][0], cycle[2][0]] 



def three_computer_connection(adj_list: dict):

    cycles = set()

    def backtrack(node: str, path: list):
        
        if len(path)==4 and path[0]==path[-1]:
            cycles.add(tuple(sorted(path[:-1])))
        
        if len(path)>4:
            return []
        
        for v in adj_list[node]:  
            backtrack(v, path+[v])
        

    nodes = {k:v for k, v in adj_list.items() if len(v)>=2}
    
    for node in nodes:
        backtrack(node, [])
    

    chief_lan = [cycle for cycle in cycles if is_chief_historian_lan(cycle)]
    return len(chief_lan)

def lan_party(adj_list: dict):

    lan_networks = set()

    def is_clique(connected_nodes, k):
        for node in connected_nodes:
            out = 0
            for neighbor in connected_nodes:
                if neighbor in adj_list[node] and neighbor!=node:
                    out+=1
            if out!=k-1:
                return False
        return True



    def find_cliques(node:str, size:int, connected_nodes: list, max_size: int):
            
        if not is_clique(connected_nodes, size):
            return []
        
        for neighbor in adj_list[node]:

            if neighbor not in connected_nodes:
                if is_clique(connected_nodes+[neighbor], size+1) and tuple(sorted(connected_nodes+[neighbor])) not in lan_networks:
                    lan_networks.add(tuple(sorted(connected_nodes+[neighbor])))
                    find_cliques(neighbor, size+1, connected_nodes+[neighbor], max_size)
    
                else:
                    return []
    
    for v in adj_list:
        
        find_cliques(v, 1, [v], -1)

    
    max_size = -1
    max_lan = None
    for lan in lan_networks:
        if len(lan)>max_size:
            max_size = len(lan)
            max_lan = lan
    return ','.join(max_lan)
   

adj_list = dict()
with open('data/input23.txt','r') as f:
    for line in f:
        edge = line.strip().split('-')
        adj_list[edge[0]] = adj_list.get(edge[0],[]) + [edge[1]]
        adj_list[edge[1]] = adj_list.get(edge[1],[]) + [edge[0]]
       
    sol1 = three_computer_connection(adj_list)

    print(sol1)


    sol2 = lan_party(adj_list)

    print(sol2)
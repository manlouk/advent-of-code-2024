def convert_disk_map(dense_representation):

    compact_representation = []

    i = 0 

    for i,c in enumerate(dense_representation):
        if i % 2==0:
            compact_representation+=int(c)*[i//2]
        else:
           
            compact_representation+=int(c)*["."]
        
    return compact_representation

def segment_of_symbols(compact_disk_map: list) -> list:
    segments = {}
    i=0
    while i < len(compact_disk_map):
        symbol = compact_disk_map[i]
        j = i
        interval = []
        while j<len(compact_disk_map) and compact_disk_map[j]==symbol:
            interval.append(j)
            j+=1
        if symbol not in segments:
            segments[symbol] = [interval]
            
        else:
            segments[symbol].append(interval)
        i+=len(interval)
    return segments



def checksum(compact_disk_map: list) -> int:
    
    segments = segment_of_symbols(compact_disk_map)
    free_spaces = segments["."]


    file_ids = sorted([file for file in segments if file!="."],reverse=True)
    segments = {k:segments[k][0] for k,_ in segments.items() if k!="."}

    for file_id in file_ids:
       for interval in free_spaces:
           if len(interval)>=len(segments[file_id]) and segments[file_id][-1]>interval[0]:
                segments[file_id] = interval[:len(segments[file_id])]
                free_spaces[free_spaces.index(interval)] = interval[len(segments[file_id]):]
                break
           

    return sum([k*sum(v) for k,v in segments.items()])


def calculate_checksum_v2(filename: str) -> int:
    
    with open(filename,'r') as f:
        disk_map = f.read().strip()
        compact_disk_map= convert_disk_map(disk_map)

        return checksum(compact_disk_map)

if __name__ == "__main__":
    print(f"Checksum v2: {calculate_checksum_v2('data/input9.txt')}")
    

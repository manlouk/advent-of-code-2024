import itertools
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def is_left(self, other):
        return self.x < other.x


def read_map(filename: str):
    with open(filename, 'r') as f:
        
        antenas_map = []
        for line in f:
            antenas_map.append([point for point in line.strip()])
        return antenas_map


def is_in_map(antenas_map, x, y)-> bool:
    return 0 <= x < len(antenas_map) and 0 <= y < len(antenas_map[0])

def get_antennas_points(antenas_map):
    antennas = {}
    
    for i, _ in enumerate(antenas_map):
        for j, _ in enumerate(antenas_map[i]):
            if antenas_map[i][j] != '.':
                if antenas_map[i][j] not in antennas:
                    antennas[antenas_map[i][j]] = set([(i, j)])
                antennas[antenas_map[i][j]].add((i, j))
    return antennas

def get_antinode_points(point_a: tuple, point_b: tuple):
   
    slope = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])

    point_left = point_a
    point_right = point_b
    if point_a[0]>point_b[0]:
        point_left = point_b
        point_right = point_a


    slope = (point_left[1] - point_right[1]) / (point_left[0] - point_right[0])
    
    
    x1 = point_left[0] - abs(point_left[0] - point_right[0])
    x2 = point_right[0] + abs(point_left[0] - point_right[0])

    y1 = point_left[1] + slope*(point_left[0] - point_right[0])
    y2 = point_right[1] - slope*(point_left[0] - point_right[0])


    return [(x1, y1), (x2, y2)]


def get_antinode_points_v2(point_a: tuple, point_b: tuple, antenas_map):

      
    point_left = point_a
    point_right = point_b
    if point_a[0]>point_b[0]:
        point_left = point_b
        point_right = point_a


    slope = (point_left[1] - point_right[1]) / (point_left[0] - point_right[0])
    
    x1 = point_left[0] - abs(point_left[0] - point_right[0])
    x2 = point_right[0] + abs(point_left[0] - point_right[0])

    y1 = point_left[1] + slope*(point_left[0] - point_right[0])
    y2 = point_right[1] - slope*(point_left[0] - point_right[0])

    antinode_points = set()

    antinode_points.add(point_left)
    antinode_points.add(point_right)
    antinode_points.add(point_a)
    antinode_points.add(point_b)

    while is_in_map(antenas_map, x1, y1):
        antinode_points.add((x1, y1))
        x1 -= abs(point_left[0] - point_right[0])
        y1 += slope*(point_left[0] - point_right[0])
    while is_in_map(antenas_map, x2, y2):
        antinode_points.add((x2, y2))
        x2 += abs(point_left[0] - point_right[0])
        y2 -=slope*(point_left[0] - point_right[0])
    
    return antinode_points


    

    


def print_map(antenas_map, antinode_points):
    for i in range(len(antenas_map)):
        for j in range(len(antenas_map[i])):
            if (i, j) in antinode_points:
                antenas_map[i][j] = "#"
    for row in antenas_map:
        print("".join(row))


    

def antinode_points(antennas_map):
    antennas = get_antennas_points(antennas_map)
    total_antinodes = set()
    for antenna in antennas:
        for point_a, point_b in itertools.combinations(antennas[antenna], 2):
            antinode_points = get_antinode_points_v2(point_a, point_b, antennas_map)
            
            #antinode_points = [point for point in antinode_points if is_in_map(antennas_map, point[0], point[1])]
            total_antinodes.update(antinode_points)
            #print(antinode_points)

    #print(total_antinodes)
    return len(total_antinodes)


if __name__ == "__main__":
    print(f"Solution: {antinode_points(read_map('data/input8.txt'))}")
from collections import Counter
def read_input(filename: str) -> tuple:
    with open(filename,'r',encoding='utf-8') as f:
        list1 = []
        list2 = []
        for line in f:
            element1, element2 = line.strip().split()
            list1.append(int(element1))
            list2.append(int(element2))
    return list1, list2


def part1(filename: str)-> int:
    list1, list2 = read_input(filename=filename)
    
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
   
    total_distance = 0
    for i, _ in enumerate(list1):
        total_distance += abs(sorted_list1[i] - sorted_list2[i])
    return total_distance

def part2(filename: str)-> int:
    list1, list2 = read_input(filename=filename)
    frequency_of_ids = Counter(list2)

    total_similarity = 0
    for element in list1:
        total_similarity+=frequency_of_ids.get(element,0) * element

    return total_similarity


if __name__ == "__main__":
    print(f"Solution for part 1: {part1(filename='data/input1.txt')}")
    print(f"Solution for part 2: {part2(filename='data/input1.txt')}")


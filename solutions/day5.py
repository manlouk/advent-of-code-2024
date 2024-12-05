import os
import timeit

def create_graph(ordering_rules: list) -> dict:

    graph = {}
    for line in ordering_rules:
        a, b = line.split("|")
        a = int(a)
        b = int(b)
        if a not in graph:
            graph[a] = []
        if b not in graph[a]:
            graph[a].append(b)
    for line in ordering_rules:
        a, b = line.split("|")
        if int(b) not in graph:
            graph[int(b)] = []
    return graph


def correctly_ordered_update(update: list, graph: dict) -> bool:

    for i in range(len(update) - 1):
        parent, child = update[i], update[i + 1]
        if child not in graph[parent]:
            return False

    return True

                


def dfs(graph, start, update, path):

    if len(path) == len(update):
        return path
    for child in graph[start]:
        if child not in path:
            result = dfs(graph, child, update, path + [child])
            if result:
                return result
    return None
    


def order_updates(update: list, graph: dict) -> list:


    update = set(update)

    pruned_graph = {}

    for parent in graph:
        if parent in update:
            pruned_graph[parent] = []
            for child in graph[parent]:
                if child in update:
                    pruned_graph[parent].append(child)

    for parent in pruned_graph:
        
        path = dfs(pruned_graph, parent, update, [parent])
        if path:
            return path
    


def find_middle_number(update) -> int:
    return update[(len(update) - 1) // 2]


def print_queue(filename: str) -> int:
    with open(filename, "r") as f:
        input = f.read()
        ordering_rules, updates = input.split("\n\n")
        ordering_rules = ordering_rules.strip().split("\n")
        updates = updates.strip().split("\n")
        graph = create_graph(ordering_rules)
        total_correct = 0
        total_incorrect = 0

        for update in updates:
            update = list(map(int, update.strip().split(",")))
            if correctly_ordered_update(update, graph):
                total_correct += find_middle_number(update)
            else:
                ordered_updates = order_updates(update, graph)
                if ordered_updates is not None:
                    total_incorrect += find_middle_number(ordered_updates)

        return total_correct, total_incorrect



if __name__ == "__main__":
    part1, part2 = print_queue("data/input5.txt")
    print(f"Solution for part 1: {part1}")
    print(f"Solution for part 2: {part2}")
    

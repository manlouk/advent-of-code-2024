import os

def eval_expression(numbers, operators)-> int:
    
    total = int(numbers[0])
    for number, operator in zip(numbers[1:], operators):
        if operator=='+':
            total+=int(number)
        else:
            total*=int(number)
    return total


def valid_test_value(target: int, numbers: list):

    result = []
    def backtrack(target, numbers):
        if eval_expression(numbers,result) == target and len(result)==len(numbers)-1:
            return True

        if len(result) == len(numbers)-1:
            return False
        else:
            result.append('*')
            if backtrack(target, numbers):
                return True
            result.pop()
            result.append('+')

            if backtrack(target, numbers):
                return True
            result.pop()

            return False

    
    return backtrack(target,numbers)
        

def part1(filename):

    with open(filename,'r') as input:
        total = 0
        for line in input:
            target, numbers = line.strip().split(':')
     
            numbers = [int(c) for c in numbers.strip().split(' ')]
            target = int(target)

            if valid_test_value(target, numbers):
                total+=target
        return total


if __name__=="__main__":
    print(f"Solution for part 1: {part1('data/input7.txt')}")



import os

def eval_expression(numbers, operators)-> int:
    
    total = int(numbers[0])
    for number, operator in zip(numbers[1:], operators):
        if operator=='+':
            total+=int(number)
        elif operator=='*':
            total*=int(number)
        else:
            total = int(str(total)+str(number))
    return total


def valid_test_value(target: int, numbers: list, symbols: list):

    result = []
    def backtrack(target, numbers):
        if eval_expression(numbers,result) == target and len(result)==len(numbers)-1:
            return True

        if len(result) == len(numbers)-1:
            return False
        else:
            for symbol in symbols:
                result.append(symbol)
                if backtrack(target, numbers):
                    return True
                result.pop()

            return False

    return backtrack(target,numbers)
        

def bridge_repair(filename):

    with open(filename,'r') as input:
        total = 0
        for i,line in enumerate(input):
            print(i)
            target, numbers = line.strip().split(':')
     
            numbers = [int(c) for c in numbers.strip().split(' ')]
            target = int(target)

            if valid_test_value(target, numbers,['*','+']) or valid_test_value(target,numbers,['+','*','||']):
                total+=target
    

        return total


if __name__=="__main__":
    print(f"Solution: {bridge_repair('data/input7.txt')}")



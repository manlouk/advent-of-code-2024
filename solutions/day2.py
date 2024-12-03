def read_input(filename: str):
    with open(filename,'r',encoding='utf-8') as f:
        for report in f:
            yield [int(level) for level in report.strip().split()]

def check_monotonicity(report: list)-> bool:
    
    return sorted(report) == report or sorted(report,reverse=True) == report

def check_difference(report: list)-> bool:
    
    for i in range(len(report)-1):
        if abs(report[i] - report[i+1]) >3 or abs(report[i] - report[i+1]) < 1:
            return False
    return True

def check_difference(report: list)-> list:
        
    return sum([abs(report[i] - report[i+1])<=3 and abs(report[i] - report[i+1])>=1  for i in range(len(report)-1)])==len(report)-1

def check_monotonicity_v2(report: list)-> bool:

    monotonous = []
    for i in range(len(report)-1):
        monotonous.append(report[i] - report[i+1] > 0)
    return all(monotonous) or not any(monotonous)

def check_safety(report: list)-> bool:
    
    return check_monotonicity_v2(report) and check_difference(report)
        
def part1(filename: str)-> int:

    total_safe = 0
    for report in read_input(filename=filename):
       if check_safety(report):
            total_safe+=1
       
    return total_safe

def part2(filename: str)-> int:
    total_safe = 0
    for report in read_input(filename=filename):
        for i in range(len(report)):
            if check_safety(report[:i]+report[i+1:]):
                total_safe+=1
                break
    return total_safe

if __name__=="__main__":
    print(f"Solution for part 1: {part1(filename='data/input2.txt')}")
    print(f"Solution for part 2: {part2(filename='data/input2.txt')}")
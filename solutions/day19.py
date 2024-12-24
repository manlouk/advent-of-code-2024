def is_possible(towel_design: str, patterns: list[str]) -> bool:

    def backtrack(towel_design: str, patterns: list[str], combination: list[str]) -> bool:
        prefix = ''.join(combination)
        if prefix == towel_design:
            return True
        if len(prefix)>=len(towel_design):
            return False
        if len(prefix)>=1 and prefix!=towel_design[:len(prefix)]:
            return False
        
        for pattern in patterns:
            if backtrack(towel_design, patterns, combination + [pattern]):
                return True
        return False


    return backtrack(towel_design, patterns, [])

def all_combinations(towel_design: str, patterns: set)-> bool:

    memoize = {}
    
    def backtrack(towel_design: str, patterns: set, combination: list[str]) -> bool:
        prefix = ''.join(combination)
        if prefix == towel_design:
            return 1
        if len(prefix)>=len(towel_design):
            return 0
        if len(prefix)>=1 and prefix!=towel_design[:len(prefix)]:
            return 0
        
        
        total_score = 0 
        for pattern in patterns:
            total_score+=backtrack(towel_design, patterns, combination+[pattern])

        return total_score
    
    return backtrack(towel_design, patterns, [])

with open('data/input19.txt','r') as f:
    input = f.read().split('\n\n')
    patterns = input[0].strip().split(',')
    patterns = [pattern.strip() for pattern in patterns]
    designs = input[1].split('\n')
    
    total = 0
    for towel_design in designs:
        dp = {'':1}
        towel = [c for c in towel_design]
        for i in range(1, len(towel_design)+1):
            ways = 0 
            if ''.join(towel[:i]) not in dp:
                dp[''.join(towel[:i])] = 0
            for pattern in patterns:
                p = [x for x in pattern]
                if len(p)<=i:
                    if towel[:i-len(p)] + p ==towel[:i]:
                        dp[''.join(towel[:i])] +=dp.get(''.join(towel[:i-len(p)]),1)
        total+=dp[towel_design] 
    print(total)
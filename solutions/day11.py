from collections import Counter

def read_input(filename: str) -> list:
    with open(filename, 'r') as input:
        return input.read().strip().split(" ")

def mutate(stone: str)-> str:

    if stone =='0':
        return ['1']
    elif len(stone) % 2 ==0:
        return [str(int(stone[:len(stone)//2])),str(int(stone[len(stone)//2:]))]
    else:
        return [str(int(stone)*2024)]

stones = read_input('data/input11.txt')

def blink(pile_old: Counter) -> Counter:
    new_pile = {}
    for stone, count in pile_old.items():
        new_stones = mutate(stone)
        if len(new_stones) == 1:
            new_pile[new_stones[0]]=  new_pile.get(new_stones[0],0) + count
        else:
            new_pile[new_stones[0]] = count + new_pile.get(new_stones[0],0)
            new_pile[new_stones[1]] = count + new_pile.get(new_stones[1],0)
        # Add the counts from the old pile to the new pile for mutated stones
        # new_pile.update({new_stone: count for new_stone in new_stones})
    return new_pile

pile = {stone: 1 for stone in stones}
for i in range(75):
    pile = blink(pile)
    print(f"New pile: {pile}")


print(sum([v for _,v in pile.items()]))
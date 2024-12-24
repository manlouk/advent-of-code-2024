import re
input = open('data/input13.txt').read().strip().split("\n\n")
input = [x.split("\n") for x in input]
input = [[re.findall(r'\d+', equation)  for equation in machine] for machine in input]
input = [[[int(x) for x in equation] for equation in machine] for machine in input]

total = 0
for machine in input:
    machine[2][0] = 10000000000000 + machine[2][0]
    machine[2][1] = 10000000000000 + machine[2][1]
    # a = machine[0][0], b = machine[1][0] c=machine[0][1] d = machine[1][1] e = machine[2][0] f = machine[2][1]
    #detA = ad - bc
    detA = machine[0][0]*machine[1][1] - machine[1][0]*machine[0][1]

    
    # invA = (1/(ad-bc)) * [de-bf, -ce+af]
    
    invA = [machine[1][1] * machine[2][0] - machine[1][0]* machine[2][1], machine[0][0]*machine[2][1] - machine[0][1]*machine[2][0]]


    sol = [invA[0]/detA, invA[1]/detA]

    if sol[0] < 0 or sol[1] < 0:
        print("No solution")

    elif detA==0:
        print("No solution")

    elif sol[0]==int(sol[0]) and sol[1]==int(sol[1]):
   
        print(sol)
        total+=sum([3*sol[0],sol[1]])
        print(sol)
print(total)

import re
from collections import Counter
for case in range(int(input())):
    instructions=input()
    while re.findall("\d\([^\)|\(]*\)",instructions)!=[]:
        #print(loops)
        for loop in re.findall("\d\([^\)|\(]*\)",instructions):
            instructions=instructions.replace(loop,int(loop[0])*loop[2:-1])
    counts=Counter(instructions)
    #print(instructions)
    print("Case #{}: {} {}".format(case+1, (0-counts["W"]+counts["E"])%(10**9)+1, (0-counts["N"]+counts["S"])%(10**9)+1))
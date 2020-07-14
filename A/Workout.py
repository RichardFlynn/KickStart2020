from math import ceil
for t in range(int(input())):
    n,k=map(int,input().split())
    mins=tuple(map(int,input().split()))
    print("Case #{}: {}".format(t,ceil(max([mins[i+1]-mins[i]for i in range(len(mins)-1)])/(k+1))))
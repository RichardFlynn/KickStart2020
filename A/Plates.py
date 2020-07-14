for t in range(int(input())):
    s,p,a=map(int,input().split())
    stacks=[tuple(map(int,input().split()))for _ in range(s)]
    print(stacks)
#    print("Case #{}: {}".format(t,))
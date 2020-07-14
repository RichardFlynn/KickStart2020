for case in range(int(input())):
    n,final=map(int,input().split())
    buses=list(map(int,input().split()))
    for i in range(n):
        while final%buses[n-1-i]:
            final-=1
    print("Case #{}: {}".format(case+1,final))
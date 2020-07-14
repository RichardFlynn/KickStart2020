for case in range(int(input())):
    n,k=map(int,input().split())
    nums=list(map(int,input().split()))
    countdown=[k-num for num in range(k)]
    counts=0
    for i in range(n-k+1):
        cd=True
        for j in range(k):
            if nums[i+j]!=countdown[j]:
                cd=False
                break
        if cd:
            counts+=1
    print("Case #{}: {}".format(case+1,counts))

for case in range(int(input())):
    n=int(input())
    heights=list(map(int,input().split()))
    count=0
    for i in range(1,n-1):
        if heights[i]>heights[i-1] and heights[i]>heights[i+1]:
            count+=1
    print("Case #{}: {}".format(case,count))
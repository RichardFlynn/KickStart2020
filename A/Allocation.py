for t in range(int(input())):
    h,b=map(int,input().split())
    prices=sorted(map(int,input().split()))
    if sum(prices)<=b:
        count=h+1
    else:
        tot=prices[0]
        count=1
        while tot<=b:
            tot+=prices[count]
            count+=1
    print("Case #{}: {}".format(t+1,count-1))
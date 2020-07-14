for case in range(int(input())):
    input()
    rec=0
    visits=map(int,input().split())
    prev=0
    maybe_rec=False
    for v in visits:
        curr=v
        if maybe_rec:
            if prev>curr:
                rec+=1
            maybe_rec=False
        if curr>prev:
            maybe_rec=True
            prev=curr
            print(prev)
    if maybe_rec:
        rec+=1
    print("Case #{}: {}".format(case+1,rec))
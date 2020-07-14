for case in range(int(input())):
    input()
    brk=0
    notes=map(int,input().split())
    prev=0
    incr=-1
    decr=0
    for n in notes:
        #print(n,prev,incr,decr)
        if n>prev:
            incr+=1
            decr=0
        elif n<prev:
            decr+=1
            incr=0
        if incr>3 or decr>3:
            brk+=1
            incr=0
            decr=0
        prev=n
    print("Case #{}: {}".format(case+1,brk))
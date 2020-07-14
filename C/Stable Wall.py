for case in range(int(input())):
    r,c=map(int,input().split())
    rows=[input()for _ in range(r)]
    supports=set()
    for col in zip(*rows):
        for i in range(r-1):
            if col[i]!=col[i+1]:
                supports.add(col[i:i+2])
        supports.add((col[r-1],"ground"))
    print(supports)
    for con in supports:
        if con[1]!='ground':
            continue
        supports.remove(con)
        unsup=False
        for con2 in supports:
            if con2[0]==con[0]:
                unsup=True
                break
        if unsup:
            continue
        print(con[0])
    print("Case #{}: {}".format(case+1,-1))
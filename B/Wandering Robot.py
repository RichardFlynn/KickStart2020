import random
for case in range(int(input())):
    width,height,holex1,holey1,holex2,holey2=map(int,input().split())
    wins=0
    runs=1000000
    for i in range(runs):
        robx,roby=(1,1)
        while True:
            if robx in range(holex1,holex2+1) and roby in range(holey1,holey2+1):
                break
            if robx==width and roby==height:
                wins+=1
                break
            if robx==width:
                roby+=1
            elif roby==height:
                robx+=1
            else:
                if random.random()<0.5:
                    robx+=1
                else:
                    roby+=1
        
    print("Case #{}: {:.5}".format(case+1,wins/runs))
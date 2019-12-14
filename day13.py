import time
def cmp(a,b):
    return (a > b) - (a < b)
def genComp(program):
    out_f=open('day13anim.txt','w')
    num={i:program[i] for i in range(len(program))}
    dirs=[(0,1),(1,0),(0,-1),(-1,0)]

    pol=[0,0]
    def comp(coins):
        num[0]=coins
        tiles={}
        px=0
        py=0
        ball_x=0
        paddle_x=0
        score=0
        dir=0
        p_mode=0
        modi=0
        po=pol[0]
        relb=pol[1]
        def store(off,value):
            num[[num[po+off],-1,relb+num[po+off]][(modi//10**off)%10]]=value
        def load(off):
            return num.get([num[po+off],po+off,relb+num[po+off]] [(modi//10**off)%10],0)
        while True: #num[po]!=99:
            comm=num[po]%100
            modi=num[po]//10
            if comm<3 or comm==7 or comm==8:
                store(3,[0,lambda a,b:a+b,lambda a,b:a*b,0,0,0,0,lambda a,b:a<b,lambda a,b:a==b][comm](load(1),load(2)))
                po+=4
            elif comm==3 or comm==99:
                for y in range(0,21):
                    ts=''
                    for x in range(0,38):
                        tile=['.','W','#','_','O'][tiles.get((x,y),0)]
                        if tile=='O':
                            ball_x=x
                        if tile=='_':
                            paddle_x=x
                        ts+=tile
                    print(ts)
                    out_f.write(ts+'\n')
                print(score)
                out_f.write(str(score)+'\n')
                time.sleep(0.05)
                store(1,-cmp(paddle_x,ball_x))
                po+=2
                if comm==99:
                    break
            elif comm==4:
                if p_mode==0:
                    px=load(1)
                elif p_mode==1:
                    py=load(1)
                else:
                    if px==-1 and py==0:
                        score=load(1)
                    else:
                        tiles[(px,py)]=load(1)
                p_mode=(p_mode+1)%3
                po+=2
            elif comm==9:
                relb+=load(1)
                po+=2
            else:
                po=[load(2),po+3][(load(1)==0)==(comm==5)]
        print('Final Score:',score)
        return tiles
    return comp

program=[int(i) for i in open("day13.txt", "r").read().split(',')]
comp=genComp(program)
tiles=comp(1)
print (sum([1 for i in tiles if tiles[i]==2]))
comp=genComp(program)
tiles=comp(2)

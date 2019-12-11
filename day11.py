def genComp(program):
    num={i:program[i] for i in range(len(program))}
    dirs=[(0,1),(1,0),(0,-1),(-1,0)]

    pol=[0,0]
    def comp(start_tile):
        tiles={(0,0):start_tile}
        x=0
        y=0
        dir=0
        p_mode=True
        modi=0
        po=pol[0]
        relb=pol[1]
        def store(off,value):
            num[[num[po+off],-1,relb+num[po+off]][(modi//10**off)%10]]=value
        def load(off):
            return num.get([num[po+off],po+off,relb+num[po+off]] [(modi//10**off)%10],0)
        while num[po]!=99:
            comm=num[po]%100
            modi=num[po]//10
            if comm<3 or comm==7 or comm==8:
                store(3,[0,lambda a,b:a+b,lambda a,b:a*b,0,0,0,0,lambda a,b:a<b,lambda a,b:a==b][comm](load(1),load(2)))
                po+=4
            elif comm==3:
                store(1,tiles.get((x,y),0))
                po+=2
            elif comm==4:
                if p_mode:
                    tiles[(x,y)]=load(1)
                else:
                    dir=(dir+[-1,1][load(1)])%4
                    x+=dirs[dir][0]
                    y+=dirs[dir][1]
                p_mode=not p_mode
                po+=2
            elif comm==9:
                relb+=load(1)
                po+=2
            else:
                po=[load(2),po+3][(load(1)==0)==(comm==5)]
        return tiles
    return comp

program=[int(i) for i in open("day11.txt", "r").read().split(',')]
comp=genComp(program)
print(len(comp(0)))
comp=genComp(program)
tiles=comp(1)
mix=min([i[0] for i in tiles])
max=max([i[0] for i in tiles])
miy=min([i[1] for i in tiles]) #max doesn't work for y, I don't know why

for y in range(0,miy-1,-1):
    ts=''
    for x in range(mix,max+1):
        ts+=['.','#'][tiles.get((x,y),0)]
    print(ts)

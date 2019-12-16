import time
dirs=[(0,0),(0,-1),(0,1),(-1,0),(1,0)]
tiles={}
front=[(0,0)]
def cmp(a,b):
    return (a > b) - (a < b)
def genComp(program):
    out_f=open('day13anim.txt','w')
    num={i:program[i] for i in range(len(program))}

    pol=[0,0]
    def comp(move):
        px=0
        py=0
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
                store(1,move)
                po+=2
            elif comm==4:
                return load(1)
                po+=2
            elif comm==9:
                relb+=load(1)
                po+=2
            else:
                po=[load(2),po+3][(load(1)==0)==(comm==5)]
        print('Final Score:',score)
        return tiles
    return comp

program=[int(i) for i in open("day15.txt", "r").read().split(',')]
comp=genComp(program)
n=1
opo=[]
out=open('day15out.txt','w')
def show():
    li=''
    for y in range(-22,22):
        for x in range(-22,21):
            li+=tiles.get((x,y),[' '])[0]
        li+='\n'
    return li
def expl(pos,ri,n):
    np=(pos[0]+dirs[ri][0],pos[1]+dirs[ri][1])
    #print(' '*n+'--',np,pos,ri,n)
    if n<8000 and (np not in tiles or (tiles[np][1]>n and tiles[np][0]=='.')):
        st=comp(ri)
        #print(st,n,np)
        if st==0:
            tiles[np]=['#',0]
            out.write(show())
        else:
            if st==1:
                tiles[np]=['.',n]
            else:
                tiles[np]=['O',n]
                opo.append(np)
                print('Oxi',np,n)
            out.write(show())
            for r in range(1,5):
                expl(np,r,n+1)
            _=comp([0,2,1,4,3][ri])

    return

for r in range(1,5):
    expl((0,0),r,1)
print(show())
li=[opo[0]]
n=0
while len(li)>0:
    out.write(show())
    nl=[]
    for p in li:
        for ri in range(1,5):
            np=(p[0]+dirs[ri][0],p[1]+dirs[ri][1])
            if tiles[np][0]=='.':
                tiles[np][0]='O'
                nl.append(np)
    li=nl
    n+=1
print(n-1)

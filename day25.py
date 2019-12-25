items=['dark matter','astrolabe','antenna','weather machine','whirled peas','fixed point','prime number','coin']
dir={'e':'east','w':'west','n':'north','s':'south'}
path='e4n7ws2nnw1esesen6seee0wwwwwn5n3es'
def genComp(program):
    num={i:program[i] for i in range(len(program))}
    pol=[0,0]
    def comp(input,output):
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
                if len(input)==0:
                    pol[0]=po
                    pol[1]=relb
                    return False
                store(1,input.pop(0))
                po+=2
            elif comm==4:
                output.append(load(1))
                po+=2
            elif comm==9:
                relb+=load(1)
                po+=2
            else:
                po=[load(2),po+3][(load(1)==0)==(comm==5)]
        print('Finish')
        return True
    return comp

program=[int(i) for i in open("day25.txt", "r").read().split(',')]
comp=genComp(program)
output=[]
inp=[]
lpath=''
for c in path:
    if c in dir:
        lpath+=dir[c]+'\n'
    else:
        lpath+='take '+items[int(c)]+'\n'
print(lpath)
inp=list(map(ord,lpath))
load=255
nload=255
while not comp(inp,output):
    instr=''
    out=''.join(map(chr,output))
    print(out)
    if out.find('lighter')<0 and out.find('heavier')<0:
        print('found')
        print(1/0)
    nload=nload-1
    print(nload)
    for i in range(8):
        if 2**i&load>0 and 2**i&nload==0:
             instr+='drop '+items[i]+'\n'
        if 2**i&load==0 and 2**i&nload>0:
            instr+='take '+items[i]+'\n'
    load=nload
    #inp=list(map(ord,input(out).strip()+chr(10)))
    inp=list(map(ord,instr+'inv\nsouth\n'))
    output=[]
print(''.join(map(chr,output)))

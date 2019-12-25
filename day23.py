idle=[False]*50
result=0
def genComp(program):
    num={i:program[i] for i in range(len(program))}
    pol=[0,0,0,False]
    def comp(input):
        modi=0
        po=pol[0]
        relb=pol[1]
        co=pol[2]
        idle=pol[3]
        #print('comp',input,po,relb)
        def store(off,value):
            #print('Store:',po+off,value)
            num[[num[po+off],-1,relb+num[po+off]][(modi//10**off)%10]]=value
        def load(off):
            #p#rint('l',(modi//10**off)%10)
            return num.get([num[po+off],po+off,relb+num[po+off]] [(modi//10**off)%10],0)
        while num[po]!=99:
            #print('po,num:',po,num[po],num[po+1],num[po+2],num[po+3],'10:',num[10])
            comm=num[po]%100
            modi=num[po]//10
            if comm<3 or comm==7 or comm==8:
                #print('3478',load(1),load(2))
                store(3,[0,lambda a,b:a+b,lambda a,b:a*b,0,0,0,0,lambda a,b:a<b,lambda a,b:a==b][comm](load(1),load(2)))
                po+=4
            elif comm==3:
                #print('inp',input)
                if len(input)>0:
                    store(1,input.pop(0))
                    idle=False
                else:
                    store(1,-1)
                    idle=True
                po+=2
            elif comm==4:
                out=load(1)
                po+=2
                pol[0],pol[1],pol[2],pol[3]=po,relb,co,idle
                return [out],idle
            elif comm==9:
                relb+=load(1)
                po+=2
            elif comm==5 or comm==6:
                #print(modi//10**1)
                #print(modi//10**2)
                #print(load(1),load(2))
                po=[load(2),po+3][(load(1)==0)==(comm==5)]
            elif comm!='99':
                print('Illegal Opcode',1/0)
            co+=1
            if co==100:
                pol[0],pol[1],pol[2],pol[3]=po,relb,0,idle
                return [],idle
    return comp

program=[int(i) for i in open("day23.txt", "r").read().split(',')]
comps=[]
input=[]
dest=[0]*50
state=[0]*50
xpuf=[0]*50
out=[]
nat=False
natx=0
naty=0
natset=set()
for i in range(50):
    comps.append(genComp(program))
    input.append([i])
    out.append([])
while True:
    for i in range(50):
        #print('Comp:',i)
        out,idle[i]=comps[i](input[i])
        #if len(out)>0:
        #    print('out',i,out)
        for n in out:
            if state[i]==0:
                dest[i]=n
            elif state[i]==1:
                xpuf[i]=n
            else:
                if dest[i]==255:
                    if result==0:
                        result=n
                    natx=xpuf[i]
                    naty=n
                    nat=True
                else:
                    input[dest[i]].append(xpuf[i])
                    input[dest[i]].append(n)
            state[i]=(state[i]+1)%3
    if nat and sum(idle)==50:
        input[0]=[natx,naty]
        #print('nn',natx,naty,natset)
        if naty in natset:
            print('Result Part 1:',result)
            print('Double y in NAT',naty)
            print(1/0)
        natset.add(naty)

def genComp(program):
    num={i:program[i] for i in range(len(program))}
    pol=[0,0,0]
    def comp(input):
        modi=0
        po=pol[0]
        relb=pol[1]
        co=pol[2]
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
                else:
                    store(1,-1)
                po+=2
            elif comm==4:
                out=load(1)
                po+=2
                pol[0],pol[1],pol[2]=po,relb,co
                return [out]
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
                pol[0],pol[1],pol[2]=po,relb,0
                return []
        print('Final Score:',score)
    return comp

program=[int(i) for i in open("day23.txt", "r").read().split(',')]
comps=[]
input=[]
dest=[0]*50
state=[0]*50
xpuf=[0]*50
out=[]
for i in range(50):
    comps.append(genComp(program))
    input.append([i])
    out.append([])
while True:
    for i in range(50):
        #print('Comp:',i)
        out=comps[i](input[i])
        if len(out)>0:
            print('out',i,out)
        for n in out:
            if state[i]==0:
                dest[i]=n
            elif state[i]==1:
                xpuf[i]=n
            else:
                if dest[i]==255:
                    print('result:',n)
                    print(1/0)
                input[dest[i]].append(xpuf[i])
                input[dest[i]].append(n)
            state[i]=(state[i]+1)%3

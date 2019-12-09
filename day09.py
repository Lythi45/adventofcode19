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
        return True
    return comp

program=[int(i) for i in open("day09.txt", "r").read().split(',')]
comp=genComp(program)
output=[]
comp([1],output)
print(output)
comp=genComp(program)
output=[]
comp([2],output)
print(output)

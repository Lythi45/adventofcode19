def genComp(program):
    num={i:program[i] for i in range(len(program))}
    pol=[0,0]
    def comp(input,output):
        modi=0
        po=pol[0]
        relb=pol[1]
        def store(off,value):
            num[[num[po+3],0,relb+num[po+3]][(modi//10**off)%10]]=value
        while num[po]!=99:
            comm=num[po]%100
            modi=num[po]//100
            n_in=[0,2,2,1,1,2,2,2,2,1][comm]
            inp=[num.get([num[po+i+1],po+i+1,relb+num[po+i+1]] [(modi//10**i)%10],0) for i in range(n_in)]
            if comm<3 or comm==7 or comm==8:
                store(2,[0,lambda a,b:a+b,lambda a,b:a*b,0,0,0,0,lambda a,b:a<b,lambda a,b:a==b][comm](inp[0],inp[1]))
                po+=4
            elif comm==3:
                if len(input)==0:
                    pol[0]=po
                    return False
                store(1,input.pop(0))
                po+=2
            elif comm==4:
                output.append(inp[0])
                po+=2
            elif comm==9:
                relb+=inp[0]
                po+=2
            else:
                po=[inp[1],po+3][(inp[0]==0)==(comm==5)]
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

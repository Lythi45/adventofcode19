import itertools

def genComp(num):
    pol=[0]
    def comp(input,output):
        po=pol[0]
        while num[po]!=99:
            comm=num[po]%100
            if comm<3 or comm==7 or comm==8:
                num[num[po+3]]=[0,lambda a,b:a+b,lambda a,b:a*b,0,0,0,0,lambda a,b:a<b,lambda a,b:a==b][comm](num[[num[po+1],po+1][(num[po]//100)%10]],num[[num[po+2],po+2][(num[po]//1000)%10]])
                po+=4
            elif comm==3:
                if len(input)==0:
                    pol[0]=po
                    return False
                num[num[po+1]]=input.pop(0)
                po+=2
            elif comm==4:
                output.append(num[[num[po+1],po+1][num[po]//100]])
                po+=2
            else:
                po=[num[[num[po+2],po+2][(num[po]//1000)%10]],po+3][(num[[num[po+1],po+1][(num[po]//100)%10]]==0)==(comm==5)]
        return True
    return comp

program=[int(i) for i in open("day07.txt", "r").read().split(',')]
thrusts=[]
for p in itertools.permutations([5,6,7,8,9]):
    first=True
    exit=False
    comps=[]
    input=[]
    for i in range(5):
        comps.append(genComp(list(program)))
        input.append([p[i]])
    input[0].append(0)
    while not exit:
        for i in range(5):
            exit=comps[i](input[i],input[(i+1)%5])
    thrusts.append(input[0][0])
print(sorted(thrusts)[-1])

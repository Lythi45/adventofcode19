import itertools

program=[int(i) for i in open("day07.txt", "r").read().split(',')]
thrusts=[]
for p in itertools.permutations([0,1,2,3,4]):
    output=[0]
    for pe in p:
        input=[pe,output.pop(0)]
        num=list(program)
        po=0
        while(num[po]!=99):
            comm=num[po]%100
            if comm<3 or comm==7 or comm==8:
                num[num[po+3]]=[0,lambda a,b:a+b,lambda a,b:a*b,0,0,0,0,lambda a,b:a<b,lambda a,b:a==b][comm](num[[num[po+1],po+1][(num[po]//100)%10]],num[[num[po+2],po+2][(num[po]//1000)%10]])
                po+=4
            elif comm==3:
                num[num[po+1]]=input.pop(0)
                po+=2
            elif comm==4:
                output.append(num[[num[po+1],po+1][num[po]//100]])
                po+=2
            else:
                po=[num[[num[po+2],po+2][(num[po]//1000)%10]],po+3][(num[[num[po+1],po+1][(num[po]//100)%10]]==0)==(comm==5)]
    thrusts.append(output[0])
print(sorted(thrusts)[-1])

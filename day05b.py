num=[int(i) for i in open("day05.txt", "r").read().split(',')]
input=[5]
po=0
while(num[po]!=99):
    print(po,num[po:po+4])
    comm=num[po]%100
    if comm<3 or comm==7 or comm==8:
        num[num[po+3]]=[0,lambda a,b:a+b,lambda a,b:a*b,0,0,0,0,lambda a,b:a<b,lambda a,b:a==b][comm](num[[num[po+1],po+1][(num[po]//100)%10]],num[[num[po+2],po+2][(num[po]//1000)%10]])
        po+=4
    elif comm==3:
        num[num[po+1]]=input[0]
        del input[0]
        po+=2
    elif comm==4:
        print(num[[num[po+1],po+1][num[po]//100]])
        po+=2
    else:
        po=[num[[num[po+2],po+2][(num[po]//1000)%10]],po+3][(num[[num[po+1],po+1][(num[po]//100)%10]]==0)==(comm==5)]

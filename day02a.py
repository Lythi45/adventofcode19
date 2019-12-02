num=[int(i) for i in open("day02.txt", "r").read().split(',')]
po=0
num[1]=12
num[2]=2
while(num[po]!=99):
    num[num[po+3]]=[0,lambda a,b:a+b,lambda a,b:a*b][num[po]](num[num[po+1]],num[num[po+2]])
    po+=4
print(num[0])

import copy
numbers=[int(i) for i in open("day02.txt", "r").read().split(',')]
for noun in range(100):
    for verb in range(100):
        num=copy.copy(numbers)
        po=0
        num[1]=noun
        num[2]=verb
        while(num[po]!=99):
            num[num[po+3]]=[0,lambda a,b:a+b,lambda a,b:a*b][num[po]](num[num[po+1]],num[num[po+2]])
            po+=4
        if num[0]==19690720:
            print(noun*100+verb)
            break

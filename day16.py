line=open('day16.txt','r').read().strip()
#line='80871224585914546619083218645595'
#line='12345678'
bas=[0,1,0,-1]
ll=len(line)
tl=[]
inp=[]
for i in range(ll):
    inp.append(int(line[i]))
    li=[]
    j=0
    while len(li)<ll+1:
        li+=[bas[j%4]]*(i+1)
        j+=1
    tl.append(li[1:ll+1])


for n in range(100):
    out=[]
    for i in range(ll):
        out.append(abs(sum([inp[j]*tl[i][j] for j in range(ll)]))%10)
    inp=out
print(''.join(map(str,out))[:8])

line=open('day16.txt','r').read().strip()
offset=int(line[:7])
bas=[0,1,0,-1]
ll=len(line)*10000

print(ll,offset)
dim=100
dll=[[1]+[0]*(dim-1)]
for i in range(ll-offset+100):
    dl=[1]
    vl=dll[-1]
    if i%100000==0:
        print(i)
    for j in range(dim-1):
        dl.append((vl[j]+vl[j+1])%10)
    dll.append(dl)
print(len(dll),dll[99][99])

nl=list(map(int,line))
ln=len(line)
ss=''
for i in range(offset,offset+8):
    su=sum([nl[j%ln]*dll[j-i+99][99] for j in range(i,ll)])%10
    print(su)
    ss+=str(su)
print(ss)

def ma(m):
    me_m=m.split()
    return (me_m[1].strip(),int(me_m[0].strip()))
matd={'ORE':0}
surplus={}
def need_ore(mat,amount):
    if mat=='ORE':
        return amount
    else:
        ra=matd[mat][0]
        of=1+(amount-1-surplus[mat])//ra
        ore = sum([need_ore(m[0],m[1]*of) for m in matd[mat][1:]])
        surplus[mat]=of*ra-amount+surplus[mat]
        #print(mat,amount,ra,of,ore,surplus[mat])
        return ore

for line in open("day14.txt", "r").readlines():
    mats=line.split('=>')
    zmat=ma(mats[1])
    surplus[zmat[0]]=0
    matd[zmat[0]]=[zmat[1]]
    for mat in mats[0].split(','):
        matd[zmat[0]].append(ma(mat))
#print(matd)
#print('sur',surplus)
no=need_ore('FUEL',1)
print(no)

val=10**12//no
mov=2**40
while mov>0:
    for i in surplus:
        surplus[i]=0
    n=need_ore('FUEL',val)
    if mov<8:
        print(n,val,mov)
    mov//=2
    val = val +(mov if n < 10**12 else -mov)

def ggT(z,n):
    while n>0:
        n,z=z%n,n
    return z
def cmp(a,b):
    return (a > b) - (a < b)
moons=[]
states=[set(),set(),set()]
zm=[0,0,0]
for moon in open("day12.txt", "r").readlines():
    moons.append([int(p.strip('yxz= ')) for p in moon.strip('<>\n').split(',')])
vel=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
def energy():
    return sum([sum(map(abs,moons[i]))*sum(map(abs,vel[i])) for i in range(4)])
z=0
zy=0
while zy<3:
    for d in range(3):
        if zm[d]==0:
            state=(moons[0][d],moons[1][d],moons[2][d],moons[3][d],vel[0][d],vel[1][d],vel[2][d],vel[3][d])
            if state in states[d]:
                zm[d]=z
                zy+=1
                print(d,z)
            states[d].add(state)

    for d in range(3):
        for m1 in range(4):
            for m2 in range(m1+1,4):
                vel[m1][d]-=cmp(moons[m1][d],moons[m2][d])
                vel[m2][d]+=cmp(moons[m1][d],moons[m2][d])
    for d in range(3):
        for m in range(4):
            moons[m][d]+=vel[m][d]
    z+=1
    if z==1000:
        print(energy())
t1=ggT(zm[0],zm[1])
z1=zm[0]*zm[1]//t1
t2=ggT(z1,zm[2])
zyklus=z1*zm[2]//t2
print(zyklus)

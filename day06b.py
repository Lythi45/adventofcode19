orb={}
for rel in [i.strip().split(')') for i in open("day06.txt", "r").readlines()]:
    orb[rel[0]]=orb.get(rel[0],[])+[rel[1]]

def osum(i):
    sans,yous=zip(*i)
    return (sum(sans)+1 if sum(sans)>0 else 0,sum(yous)+1 if sum(yous)>0 else 0)

def orbits(obj):
    #print(obj)
    if obj =='SAN':
        return (1,0)
    if obj=='YOU':
        return (0,1)
    s=osum([orbits(i) for i in orb[obj]])  if obj in orb else (0,0)
    #print(s)
    if s[0]>0 and s[1]>0:
        print (s[0]+s[1]-4)
        return (0,0)
    return s

orbits('COM')

orb={}
for rel in [i.strip().split(')') for i in open("day06.txt", "r").readlines()]:
    orb[rel[0]]=orb.get(rel[0],[])+[rel[1]]

def osum(i):
    orbs,objs=zip(*i)
    return (sum(orbs)+sum(objs),sum(objs)+1)

def orbits(obj):
    return osum([orbits(i) for i in orb[obj]])  if obj in orb else (0,1)

print(orbits('COM')[0])

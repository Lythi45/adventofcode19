import math

def ggT(z,n):
    while n>0:
        n,z=z%n,n
    return z
def short(dx,dy):
    t=ggT(dx,abs(dy))
    return (dx/t,dy/t)
def angle(dx,dy):
    return -math.atan2(dx,dy)


asters=[]
for y,line in enumerate(open("day10.txt", "r").readlines()):
    for x,char in enumerate(line):
        if char=='#':
            asters.append((x,y))
dist_dict={}
for aster in asters:
    dist_set=set()
    for aster2 in asters:
        if aster2!=aster:
            dist_set.add(short(aster2[0]-aster[0],aster2[1]-aster[1]))
    dist_dict[aster]=len(dist_set)
best_aster=sorted(dist_dict,key=lambda a:dist_dict[a])[-1]
print(best_aster,dist_dict[best_aster]+1)#dont know why I have to add 1
ang_dict={}
for aster in asters:
    if aster!=best_aster:
        dx=aster[0]-best_aster[0]
        dy=aster[1]-best_aster[1]
        ang=angle(dx,dy)
        ang_dict[ang]=ang_dict.get(ang,[])+[(dx,dy)]
ang_dict2={}
for ang in ang_dict:
    sast=sorted(ang_dict[ang],key=lambda a:a[0]*a[0]+a[1]*a[1])
    for i,ast in enumerate(sast):
        ang_dict2[ang+8*i]=ast
sang=sorted(ang_dict2)
#for i,ang in enumerate(sang):
#    ast=ang_dict2[ang]
#    print(i,ast[0]+best_aster[0],ast[1]+best_aster[1])
aster200=ang_dict2[sang[199]]
print((aster200[0]+best_aster[0])*100+(aster200[1]+best_aster[1]))

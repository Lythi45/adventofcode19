mod=False
cross=set()
wire=set()
drc={'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1)}
for i in open("day03.txt", "r").readlines():
    x,y=0,0
    for r in i.split(','):
        ri=r[0]
        for j in range(int(r[1:])):
            x+=drc[ri][0]
            y+=drc[ri][1]
            if mod:
                if (x,y) in wire:
                    cross.add((x,y))
            else:
                wire.add((x,y))
    mod=True
print(cross)
mid=9999999999
micr=(0,0)
for cr in cross:
    di=abs(cr[0])+abs(cr[1])
    if di<mid:
        mid=di
        micr=cr
print (micr,mid)

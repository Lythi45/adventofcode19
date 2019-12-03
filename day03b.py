mod=False
cross=set()
wire={}
drc={'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1)}
for i in open("day03.txt", "r").readlines():
    x,y=0,0
    l=0
    for r in i.split(','):
        ri=r[0]
        for j in range(int(r[1:])):
            x+=drc[ri][0]
            y+=drc[ri][1]
            l+=1
            if mod:
                if (x,y) in wire:
                    cross.add(l+wire[(x,y)])
            else:
                wire[(x,y)]=l
    mod=True
print(cross)
mid=9999999999
for di in cross:
    if di<mid:
        mid=di
print (mid)

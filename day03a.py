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

print(sorted([abs(i[0])+abs(i[1]) for i in cross])[0])

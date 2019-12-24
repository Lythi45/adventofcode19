dir=[(0,1),(1,0),(0,-1),(-1,0)]
nums=set()
lines=open('day24.txt','r').readlines()
tiles=['.......']
for l in lines:
    tiles.append('.'+l.strip()+'.')
tiles.append('.......')
print(tiles)
def cn(x,y):
    ne=0
    for ri in range(4):
        ne+=tiles[y+dir[ri][0]][x+dir[ri][1]]=='#'
    return ne

while True:
    ntiles=['.......']
    nu=0
    for y in range(1,6):
        nt='.'
        for x in range(1,6):
            bug=tiles[y][x]
            ne=cn(x,y)
            if bug=='#' and ne!=1:
                nb='.'
            elif bug=='.' and (ne==1 or ne==2):
                nb='#'
            else:
                nb=bug
            nt+=nb
            nu=nu//2+(bug=='#')*2**24
        ntiles.append(nt+'.')
    ntiles.append('.......')
    tiles=ntiles
    print(tiles,nu)
    if nu in nums:
        print(nu)
        break
    else:
        nums.add(nu)

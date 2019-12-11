import random
def color(n):
    return '\u001b['+str(n+30)+';1m'
def line_of_tree(treewidth,center):
    print(' '*(center-treewidth//2)+''.join([color((lambda r: r if r <8 else 2 )(random.randint(1,13)))+'*' for _ in range(treewidth)]))
height=20
center=25
width=1
for i in range(height):
    width+= -2 if i%5==0 else 2
    line_of_tree(width,center)
for _ in range(3):
    line_of_tree(3,center)

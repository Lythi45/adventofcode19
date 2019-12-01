print(sum([(lambda a:lambda v:a(a,v))(lambda weight,sf:sf[0] if sf[1]<=6 else weight(weight,(sf[0]+sf[1]//3-2,sf[1]//3-2)))(i) for i in [(0,int(i)) for i in open("day01a.txt", "r").readlines()]]))

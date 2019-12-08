print(''.join([open("day08.txt", "r").read()[i::25*6].strip('2')[0]+['','\n'][i%25==24] for i in range(25*6)]).translate({ord('1'):'#',ord('0'):' '}))

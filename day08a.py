from textwrap import wrap
image=sorted(wrap(open("day08.txt", "r").read(),25*6),key=lambda image:sum([1 for pixel in image if pixel=='0']))[0]
print(sum([1 for pixel in image if pixel=='1'])*sum([1 for pixel in image if pixel=='2']))

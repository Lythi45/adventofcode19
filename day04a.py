num=0
for n in range(240298,784957):
    s=str(n)
    fl1=False
    fl2=True
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            fl1=True
        if s[i]>s[i+1]:
            fl2=False
    if fl1 and fl2:
        num+=1
print(num)

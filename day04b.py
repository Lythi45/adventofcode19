num=0
for n in range(240298,784957):
    s='#'+str(n)+'#'
    fl1=False
    fl2=True
    for i in range(1,len(s)-2):
        if s[i]==s[i+1]and s[i-1]!=s[i]and s[i+1]!=s[i+2]:
            fl1=True
        if s[i]>s[i+1]:
            fl2=False
    if fl1 and fl2:
        print(n)
        num+=1
print(num)

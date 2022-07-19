a='abcdefghistuv'
s='jklmnopqrwxyz'
t='ocjp{zkirjwmo-ollj-nmlw-joxi-tmolnrnotvms}'
f=[]
len=len(t)
for i in range(0,len):
    n=a.find(t[i])
    m=s.find(t[i])
    if n==-1 and m==-1:
        f.append(t[i])
    if n==-1 and m!=-1:
      f.append(a[m])
    elif m==-1 and n!=-1:
        f.append(s[n])
for i in range(0,len):
  print(f[i],end="")
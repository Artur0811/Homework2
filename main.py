with open ("26 (1).txt") as f :
    n = f.readline()
    a = []
    for i in f:
        a.append(list(map(int, i.split())))
r = []
s = 0
for i in range(len(a)):
    if a[i][0]<=1634515200 and a[i][1]>1634515200 or a[i][0]<=1634515200 and a[i][1]==0:
        s+=1
    if 1634515200 < a[i][0]< 1634515200+7*24*3600:
        r.append([a[i][0], 0])
    if 1634515200 < a[i][1]< 1634515200+7*24*3600:
        r.append([a[i][1], 1])
r=sorted(r, key=lambda x:x[0])
sm = s
t = 0
for i in range(len(r)):
    if r[i][1] == 0:
        s+=1
        tn = r[i][0]
    else:
        s-=1
    if sm < s:
        sm = s
        if i+1 != len(r):
            if r[i+1][1] == 1:
                t= r[i+1][0] - tn
        else:
            t = 1634515200+7*24*3600-tn
print(sm, t)
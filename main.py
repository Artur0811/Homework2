#большое число
def number():
    n = "9"*199090+"0"*10+"1"*900
    k = int(input())
    num = {i:n.count(str(i)) for i in range(10)}
    for i in num:
        a = num[i]
        if k > a:
            k-=a
            n =n.replace(str(i), "")
        else:
            n = n.replace(str(i), "", k)
            break
    print(n)

n = int(input())
m = [int(input()) for i in range(n)]
p = [0]*n
p[0] = m[0]
mp = []
for i in range(1, n):
    if p[i-1] > 0 and m[i] > 0:
        p[i] = m[i]
        mp.append(i)
    elif m[i]<= 0 and p[i-1] + m[i] > 0:
        p[i] = m[i] + p[i-1]
    elif p[i-1] > 0 and p[i-1] + m[i]<= 0:
        p[i] = m[i]
        mp.append(i)
    else:
        p[i] = m[i] + p[i - 1]
    if len(mp) ==2:
        break
ml =[]
l = [0]*n
l[-1] = m[-1]
for i in range(-2, -n-1, -1):
    if l[i+1]+m[i]>0 and m[i]<0:
        l[i] = m[i]+l[i+1]
    elif l[i+1]>0 and l[i+1]+m[i]<=0:
        l[i] = m[i]
        ml=[n+i+1]+ml
    elif l[i+1]>0 and m[i] > 0:
        l[i] = m[i]
        ml=[n+i+1]+ml
    else:
        l[i] = m[i] + l[i + 1]
    if len(ml) ==2:
        break
if len(mp) == 2:
    print(mp[0], mp[1]-mp[0], n- mp[1])
elif len(mp) == 1 and len(ml) == 1:
    if mp[0] < ml[0]:
        print(mp[0], ml[0]-mp[0], n - ml[0])
elif len(ml) == 2:
    print(ml[0], ml[1] - ml[0], n-ml[1])
else:
    print(0)
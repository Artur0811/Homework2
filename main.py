s = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
def f(num, s, per = ""):
    zn = {}
    zn[0] = ""
    raz = 1
    for i in range(len(s)):
        if i%2 == 0:
            for y in range(1, 4):
                zn[raz*y] = s[i]*y
            if i != len(s)-1:
                zn[4*raz] = s[i]+s[i+1]
            if i!= 0:
                zn[9*raz//10] = s[i-2]+s[i]
        else:
            for y in range(4):
                zn[raz*(5+y)] = s[i]+ s[i-1]*y
            raz = raz*10
    raz = 10**(len(str(num))-1)
    while raz > 0:
        if raz == 1:
            per += zn[num%10]
        else:
            per += zn[num//raz*raz]
        num = num - num // raz * raz
        raz = raz//10
    return per

for i in range(2900, 3000):
    print(f(i, s), i)

rez = []
def f1(m, p):
    m = sorted(m)
    len_m = len(m)
    s = {}
    for i in m:
        s[i] = m.count(i)
    for i in range(len_m):
        for y in range(i+2, len_m):
            k = i+1
            while k < y:
                if p - m[i] - m[y] - m[k] in s:
                    el = p - m[i] - m[y] - m[k]
                    zn = sorted([m[i], m[k], m[y],el])
                    if zn not in rez and zn.count(el)<= s[el]:
                        rez.append(zn)
                k += 1
f1([1,0,-1,0,-2,2], 0)
for i in rez:
  print(i)

def moda(a, b):
    c = []
    k =0
    n = 0
    while k < len(a) and n < len(b):
        if a[k] > b[n]:
            c.append(b[n])
            n+=1
        else:
            c.append(a[k])
            k+=1
    c+=a[k:]
    c+=b[n:]
    print(c)
    if len(c)%2 == 1:
        return c[len(c)//2]
    else:
        return (c[len(c)//2] + c[len(c)//2-1])/2

print(moda([1, 3, 6, 9, 19], [-4, -2, 0, 28, 99]))
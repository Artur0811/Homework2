def n26_1():
    s = {}
    with open("f.txt") as f:
        n = f.readline()
        for i in f:
            a,b = map(int, i.split())
            if a not in s:
                s[a] = [b]
            else:
                v = s[a]
                v.append(b)
                v =sorted(v)
                s[a] = v
    ma, m = 0, 0
    for i in s:
        v = s[i]
        for y in range(len(v)-1):
            if v[y+1]-v[y] == 3:
                if i > ma:
                    ma = i
                    m = v[y]+1
                break
    print(ma, m)#8631 7311

def n26_2():
    with open("f.txt") as f:
        s, n = map(int, f.readline().split())
        a = sorted(map(int, f))
        k,ma = 0, 0
        for i in range(len(a)):
            if s - a[i] >= 0:
                s-=a[i]
                k+=1
                ma= a[i]
            else:
                break
        ma +=s
        while ma not in a:
            ma-=1
        print(k, ma)#729 23

def n27_1():
    with open("f.txt") as f:
        n = f.readline()
        a = list(map(int, f))
        su = sum(a)
        r = []
        r.append(a[0])
        for i in range(1, len(a)):
            r.append(r[-1] + a[i])
        l = []
        l.append(a[-1])
        for i in range(-2, -len(a)-1, -1):
            l = [l[0]+a[i]] + l
        k = len(list(filter(lambda x : x%999 == 0, a)))
        for i in range(0, len(a)):
            for y in range(i+1, len(a)):
                s = su - r[i] - l[y]+a[i]+a[y]
                if s%999 == 0:
                    k+=1
        print(k)#a- 403

with open("f.txt") as f:
    n = f.readline()
    d1 = []
    d2 = []
    s = 0
    for i in f:
        a, b= map(int, i.split())
        s+=min(a, b)
        if abs(a-b)%3 == 1:
            d1.append(abs(a-b))
        if abs(a-b)%3 == 2:
            d2.append(abs(a-b))
    if s%3 != 0:
        print(s)
    else:
        d1 =sorted(d1)
        d2 =sorted(d2)
        m =[]
        if len(d1) >1:
            m.append(s+d1[0]+d1[1])
        if len(d2) > 0:
            m.append(s+d2[0])
        if len(d1) > 0:
            m.append(s+d1[0])
        if len(d2) > 1:
            m.append(s+ d2[0]+d2[1])
        print(min(m))
        #a - 67088 b - 200157478
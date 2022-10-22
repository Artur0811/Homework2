def n2():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (not(x<=w) or (y==z) or y) ==0:
                        print(x,y,z,w)
def n5():
    for i in range(1000, 10000):
        a = str(i)
        b = int(a[0])*int(a[1])
        c = int(a[2])*int(a[3])
        if b > c:
            d = str(b)+str(c)
        else:
            d = str(c)+str(b)
        if d == "124":
            print(i)
            break

def n12():
    a = "1"*66
    while "111" in a:
        a = a.replace("111", "2", 1)
        a = a.replace("222", "3", 1)
        a = a.replace("333", "1",1)
    print(a)

def n14():
    a = 2* (216**8) + 4*(36**12) +6**15 - 1296
    b = ""
    while a > 0:
        b+=str(a%6)
        a = a//6
    print(b.count("0"))

def n15():
    def TRI(n):
        if n == 1:
            return 0
        if n == 2 or n == 3:
            return 1
        else:
            return TRI(n-3) + TRI(n-2)+TRI(n-1)
    print(TRI(10))

def n17():
    k=0
    su = 0
    with open("f") as f:
        a = list(map(int, f))
        sr = sum(a)/len(a)
        for i in range(len(a)-1):
            if a[i]%5 == 0 or a[i+1]%5 == 0 and a[i]<sr or a[i+1]<sr:
                k+=1
                if su < a[i]+a[i+1]:
                    su = a[i]+a[i+1]
    print(k, su)
def n20():
    def f(x, h):
        if x >= 42 or h > 4:
            return h==4
        if h == 2:
            return f(x+1, h+1) and f(x+5, h+1) and f(x*3, h+1)
        return f(x + 1, h + 1) or f(x + 5, h + 1) or f(x * 3, h + 1)
    for i in range(1, 42):
        if f(i, 1):
            print(i)

def n21():
    def f(x, h):
        if x >= 42 and (h==3 or h ==5):
            return True
        if x >= 42 and (h==2 or h ==4) or h >5:
            return False
        if h%2 == 1:
            return f(x + 1, h + 1) and f(x + 5, h + 1) and f(x * 3, h + 1)
        return f(x + 1, h + 1) or f(x + 5, h + 1) or f(x * 3, h + 1)


    for i in range(1, 42):
        if f(i, 1):
            print(i)
def n23():
    def f(x, y):
        if x == y:
            return 1
        if x > y:
            return 0
        return f(x+1, y)+f(2*x, y) + f(2*x+1, y)
    print(f(2, 16))

def n24():
    with open("f") as f:
        n = 99999999999999999999999999
        for i in f:
            if i.count("N") < n:
                n = i.count("N")
                s = sorted(list(set(i.strip())))
                k,b = 0, ""
                for y in range(len(s)):
                    if i.count(s[y]) >= k:
                        k = i.count(s[y])
                        b = s[y]
        print(b)

def n25():
    s = 0
    n = 0
    for i in range(120115, 120201):
        k = 0
        for y in range(1, round(i**0.5)+1):
            if i%y == 0:
                if i%y == y:
                    k +=1
                else:
                    k+=2
        if k >= s:
            s = k
            n = i
    print(s, n)

def n26():
    with open("f") as f:
        s, n = map(int, f.readline().split())
        k = 0
        m= 0
        a = sorted(map(int, f))
        for i in range(len(a)):
            if s-a[i] > 0:
                k+=1
                m = a[i]
                s-=a[i]
            else:
                break
        m+=s
        while m not in a:
            m-=1
        print(k, m)

with open("f") as f:
    n = f.readline()
    a = list(map(int, f))
    delit  = list(filter(lambda x:x%17 == 0, a))
    ndelit  = list(filter(lambda x:x%17 > 0, a))

    delit_ch = sorted(filter(lambda x:x%2 == 0, delit))
    delit_nch = sorted(filter(lambda x: x % 2 == 1, delit))

    ndelit_ch = sorted(filter(lambda x: x % 2 == 0, ndelit))
    ndelit_nch = sorted(filter(lambda x: x % 2 == 1, ndelit))

    m = []
    if delit_ch != [] and ndelit_ch != []:
        if len(delit_ch) >1:
            m.append([delit_ch[-1]+delit_ch[-2], [delit_ch[-1],delit_ch[-2]]])
        m.append([delit_ch[-1] + ndelit_ch[-1], [delit_ch[-1] , ndelit_ch[-1]]])
    elif delit_nch != [] and ndelit_nch != []:
        if len(delit_nch) >1:
            m.append([delit_nch[-1]+delit_nch[-2], [delit_nch[-1],delit_nch[-2]]])
        m.append([delit_nch[-1] + ndelit_nch[-1], [delit_nch[-1] , ndelit_nch[-1]]])
    print(max(m, key=lambda x:x[0]))
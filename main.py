def n12():
    a = ">"+"1"*10 + "2"*20 +"3"*30
    while ">1" in a or ">2" in a or ">3" in a:
        if ">1" in a:
            a = a.replace(">1" ,"22>" ,1)
        elif ">2" in a:
             a = a.replace(">2", "2>", 1)
        else:
            a = a.replace(">3", "1>",1)
    k = 0
    for i in range(len(a)-1):
        k+=int(a[i])
    print(k)
def n14():
    a = 36**7 + 6**19 - 18
    b = ""
    while a > 0:
        b+=str(a%6)
        a = a//6
    print(b.count("5"))
def n15():
    for a in range(1000):
        t = True
        for x in range(1000):
            for y in range(1000):
                if not((3*x + 4*y != 70) or (a > x) or (a>y)):
                    t = False
                    break
            if not(t):
                break
        if t:
            print(a)
            break

def n16():
    def f(n):
        if n == 1 or n == 2:
            return 1
        return f(n-2) * (n-1)
    print(f(8))

def n17():
    k = 0
    ma = 0
    with open("f") as f:
        a = list(map(int, f))
        for i in range(len(a)):
            for y in range(i+1, len(a)):
                if a[i]%31 == 0 or a[y]%31 == 0:
                    if abs(a[i] - a[y])%2 == 0:
                        k+=1
                        if ma< a[i] + a[y]:
                            ma = a[i] + a[y]
    print(k, ma)

def n21():
    def f(x, y, h):
        if x+y >= 82 and (h == 5 or h== 3):
            return True
        if x + y >= 82 and (h == 4 or h == 2) or h > 5:
            return False
        if h%2 == 1:
            return f(x+1, y, h+1) and f(x, y+1, h+1) and f(x*4, y , h+1) and f(x, y*4, h+1)
        return f(x+1, y, h+1) or f(x, y+1, h+1) or f(x*4, y , h+1) or f(x, y*4, h+1)
    for i in range(1, 78):
        if f(4, i ,1):
            print(i)

def n23():
    def f(x, y):
        if x > y or x == 6 or x == 12:
            return 0
        if x == y:
            return 1
        return f(x+1, y) + f(x*2, y) + f(x+3, y)
    print(f(3, 16))

def n24():
    with open("24 (4).txt") as f:
        m , v = 0, ""
        a = f.read().strip()
        b = {}
        for i in range(1, len(a)-1):
            if a[i-1] == a[i+1]:
                if a[i] in b:
                    b[a[i]]+=1
                else:
                    b[a[i]] = 1
        for i in b:
            if b[i] > m:
                m =b[i]
                v = i
        print(v)

def n25():
    for i in range(289123456, 389123457):
        if round(i**0.5)**2 == i:
            m = 0
            k = 0
            for y in range(2, round(i**0.5)):
                if i%y == 0:
                    k+=2
                    if i//y > m:
                        m = i//y
                if k > 2:
                    break
            if k == 2:
                print(i, m)

def n26():
    with open("f") as f:
        n,m = map(int, f.readline().split())
        a =[]
        b = []
        for i in f:
            c = i.split()
            if c[2] == "A":
                a.append([int(c[0]), int(c[1])])
            if c[2] == "B":
                b.append([int(c[0]), int(c[1])])
        a = sorted(a, key=lambda x: x[0])
        b = sorted(b, key=lambda x: x[0])
        for i in range(len(a)):
            if m- a[i][0]*a[i][1] > 0:
                m -=a[i][0]*a[i][1]
            else:
                pr = a[i][1]
                while pr > 0:
                    if m- a[i][0]*pr > 0:
                        m-=a[i][0]*pr
                        break
                    pr -=1
        kol = 0
        for i in range(len(b)):
            if m- b[i][0]*b[i][1] > 0:
                m -=b[i][0]*b[i][1]
                kol += b[i][1]
            else:
                pr = b[i][1]
                while pr > 0:
                    if m- b[i][0]*pr > 0:
                        kol += pr
                        m-=b[i][0]*pr
                        break
                    pr -=1
        print(m, kol)

def n27():
    with open("f") as f:
        n = f.readline()
        s = 0
        m = []
        for i in f:
            a = list(map(int, i.split()))
            s+=max(a)
            m.append(abs(a[0] - a[1]))
        if s%3 == 0:
            print(s)
        elif s%3 ==1:
            print(max(s- sorted(filter(lambda x:x%3 == 1, m))[0], s- sorted(filter(lambda x:x%3 == 2, m))[0]-sorted(filter(lambda x:x%3 == 2, m))[1]))
        else:
            print(max(s- sorted(filter(lambda x:x%3 == 1, m))[0]- sorted(filter(lambda x:x%3 == 1, m))[1], s- sorted(filter(lambda x:x%3 == 2, m))[0]))

n27()
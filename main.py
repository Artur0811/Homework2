def n2():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((x and y) or (y == z) or w) == 0:
                        print(x, y, z,w)

def n5():
    for i in range(1000, 10000):
        a = str(i)
        b = sorted([int(a[0]) + int(a[1]), int(a[1]) + int(a[2]), int(a[2]) + int(a[3])])[1:]
        c = str(b[0]) + str(b[1])
        if c == "1215":
            print(i)
            break

def n6():
    import turtle as t
    t.left(90)
    for i in range(4):
        t.forward(9*25)
        t.right(90)
    for i in range(3):
        t.forward(9*25)
        t.right(120)
    t.up()
    for x in range(-1, 11):
        for y in range(-1, 11):
            t.goto(x*25, y*25)
            t.dot(3)
    t.done()

def n8():
    a = sorted("АЛГОРИТМ")
    k = 0
    for i in a:
        for x in a:
            for y in a:
                for z in a:
                    k +=1
                    if i+x == "ИГ":
                        print(k)
                        break

def n14():
    for x in range(9):
        for y in range(9):
            a = int("88" + str(x) + "4" + str(y), 9)+int("7" + str(x) + "44" + str(y), 11)
            if a%61 == 0:
                print(a//61)

def n15():
    for a in range(1000):
        t = True
        for m in range(1000):
            for n in range(1000):
                if not((2*m + 3*n > 40) or ((m < a) and (n <= a))):
                    t = False
                    break
            if not(t):
                break
        if t:
            print(a)
            break

def n16():
    def f(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        return f(n-3)*n
    print(f(10))

def n17():
    k = 0
    s  = 0
    with open("f") as f:
        a = list(map(int, f))
        for i in range(len(a)):
            for y in range(i+1, len(a)):
                if (a[i]*a[y])%62 == 0:
                    k+=1
                    s = max(s, a[i] + a[y])
    print(k, s)

def n19():
    def f(x, h):
        if x >= 64 or h >3:
            return h == 3
        if h == 2:
            return f(x + 1, h + 1) and f(x * 3, h + 1)
        return f(x + 1, h + 1) or f(x * 3, h + 1)
    for i in range(1, 64):
        if f(i, 1):
            print(i)
            break

def n20():
    def f(x, h):
        if x >= 64 or h >4:
            return h == 4
        if h%2==0:
            return f(x + 1, h + 1) and f(x * 3, h + 1)
        return f(x + 1, h + 1) or f(x * 3, h + 1)
    for i in range(1, 64):
        if f(i, 1):
            print(i)

def n21():
    def f(x, h):
        if x >= 64 and (h==5 or h == 3):
            return True
        if x >= 64 and (h==2 or h == 4) or h > 5:
            return False
        if h%2==1:
            return f(x + 1, h + 1) and f(x * 3, h + 1)
        return f(x + 1, h + 1) or f(x * 3, h + 1)
    for i in range(1, 64):
        if f(i, 1):
            print(i)

def n23():
    def f(x, y):
        if  x > y:
            return 0
        if x == y:
            return 1
        return f(x+1, y) + f(x*2, y) + f(x+3, y)
    print(f(3, 12) *f(12, 16))

def n24():
    with open("f") as f:
        a = f.readline().strip()
        k =0
        l =0
        pl = 0
        while k < len(a)-2:
            if a[k]+a[k+1] + a[k+2] == "LDR":
                k+=3
                pl +=3
            else:
                if a[k] + a[k+1] == "LD":
                    pl +=2
                    k+=1
                if a[k] == "L":
                    pl += 1
                k+=1
                l = max(l, pl)
                pl = 0
        l = max(l, pl)
        print(l)

def n25():
    z = []
    m = 0
    for i in range(84052, 84131):
        d = []
        for y in range(1, round(i**0.5)+1):
            if i%y == 0:
                if y!= i//y:
                    d.append(y)
                    d.append(i//y)
                else:
                    d.append(y)
        if len(d) > m:
            m = len(d)
            z = [i]
        elif len(d) == m:
            z.append(i)
    print(m, min(z))

def n26():
    k, ma =0, 0
    with open("f") as f:
        s, n = map(int, f.readline().split())
        a = sorted(map(int, f))
        for i in range(len(a)):
            if s- a[i] >= 0:
                s-=a[i]
                k+=1
                ma = a[i]
            else:
                break
        ma += s
        while ma not in a:
            ma -=1
        print(k, ma)

def n27():
    with open("f") as f:
        n = f.readline()
        s = 0
        ed = []
        dv = []
        for i in f:
            a = sorted(map(int, i.split()))
            s+=a[0]
            if (a[1]-a[0])%3 == 1:
                ed.append(a[1]-a[0])
            if (a[1]-a[0])%3 == 2:
                ed.append(a[1]-a[0])
        if s%3 != 0:
            print(s, 1)
        else:
            ed = sorted(ed)
            dv = sorted(dv)
            m = []
            if dv != []:
                m.append(s+dv[0])
            if ed != []:
                m.append(s+ed[0])
            print(min(m), 2)
n6()

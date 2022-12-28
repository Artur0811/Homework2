def n2():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    print(x, y, z, w, (x == (not y)) <= ((z <= (not w)) and (w <= y)))
def n5():
    def f(n):
        s = 0
        for i in range(len(str(n))):
            s+= int(str(n)[i])
        if s%2 == 0:
            a = bin(n)[2:] + "0"
        else:
            a = bin(n)[2:] + "1"
        return int(a, 2)
    k = 1
    a = f(f(f(k)))
    while a <=1028:
        k+=1
        a = f(f(f(k)))
        print(a, k)

def n6():
    import turtle as t
    t.left(90)
    for i in range(4):
        t.forward(7*20)
        t.right(90)
        t.forward(7 * 20)
        t.left(90)
        t.forward(7 * 20)
        t.right(90)
    t.up()
    for x in range(-1, 30):
        for y in range(-16, 16):
            t.goto(x*20, y*20)
            t.dot()
    t.done()
def n8():
    k = 0
    a = "ВЕРОНИКА"
    b = "ЕОИА"
    for i in a:
        for x in a:
            for y in a:
                for z in a:
                    for w in a:
                        for q in a:
                            c = 0
                            d = 0
                            s = i+x+y+z+w+q
                            for j in range(6):
                                if s[j] in b:
                                    c+=1
                                else:
                                    d+=1
                            if c > d:
                                k+=1

def n9():
    k = 0
    with open("f") as f:
        for i in f:
             a = list(map(int, i.split()))
             b ,c =list(filter(lambda x:x%2 == 1, a)), list(filter(lambda x:x%2 == 0, a))
             if len(b) > len(c) and sum(b) < sum(c) and len(set(a)) == len(a):
                 k+=1
    print(k)

def n14():
    for x in range(37):
        a = "1230"[::-1]
        b = "4059"[::-1]
        s = 0
        for y in range(4):
            s+=(int(a[y]) + int(b[y]))*(37**y)
        s+=x
        s+=x*(37**2)
        if s%36 == 0:
            print(s/36)
def n15():
    for a in range(1, 1000):
        t = True
        for x in range(1, 1000):
            for y in range(1, 1000):
                if not((144%x == 0)<= (not(x%y == 0)) or (x + y > 100) or (a - x > y)):
                    t = False
        if t:
            print(a)

def n17():
    with open("f") as f:
        a = list(map(int, f))
        m = min(list(filter(lambda x:x%5 ==0, a)))
        k = 0
        ma = 0
        for i in range(len(a)-1):
            if min(a[i], a[i+1])%5 == 0 and (a[i]**2 + a[i+1]**2)<(m**2):
                k+=1
                if ma < a[i] + a[i+1]:
                    ma = a[i] + a[i+1]
    print(ma, k)

def n21():
    def f(x, y, h):
        if x+y >= 81 and (h==5 or h == 3):
            return True
        if x + y >= 81 and (h == 2 or h == 4) or h > 5:
            return False
        if h%2 == 1:
            if x < y:
                return f(x + 1, y, h + 1) and f(x + 2, y, h + 1) and f(x * 2, y, h + 1)
            return f(x, y + 1, h + 1) and f(x, y + 2, h + 1) and f(x, y * 2, h + 1)
        if x < y:
            return f(x+1, y, h+1) or f(x+2, y, h+1) or f(x*2, y, h+1)
        return f(x, y+1, h+1) or f(x, y+2, h+1) or f(x, y*2, h+1)
    for i in range(1, 69):
        if f(12, i, 1):
            print(i)

def n23():
    def f(x, y, k, p):
        if k ==0:
            return f(x+1, y, 1, 1) + f(x*2, y, 1, 2)
        if x == y:
            return 1
        if x > y:
            return 0
        if k == 2:
            if p == 1:
                return f(x*2, y, 1, 2)
            else:
                return f(x+1, y, 1, 1)
        if p == 1:
            return f(x+1, y, k+1, 1) + f(x*2, y, 1, 2)
        return f(x+1, y, 1, 1) + f(x*2, y, k+1, 2)
    print(f(1, 16, 0 ,0))

def n24():
    with open("f") as f:
        a = f.read().strip().split("D")
        b = list(filter(lambda x:x.count("O")<=2, a))
        c = list(map(lambda x: len(x)+2, b))
        if b[0] == a[0]:
            c[0]-=1
        if b[-1] == a[-1]:
            c[-1] -=1
        print(max(c))
def n25():
    k = 0
    for x in range(0, 1000):
        for y in range(10):
            for z in range(10):
                a = int("12" + str(x) + "93" + str(y) + "1" + str(z))
                if a <10**9 and a%3127 == 0:
                    print(a)
                    k+=1
    print(k)

def n26():
    with open("f") as f:
        a = []
        b = []
        for i in f:
            c = i.split()
            if c[1] == "A":
                a.append(int(c[0]))
            else:
                b.append(int(c[0]))#сортирую контейнеры
        a = sorted(a)[::-1]
        b = sorted(b)[::-1]
        ka = 0#шаг в контейнерах а
        kb = 0#шаг в контейнерах б
        v = 0# сколько вложено на данный момент
        kol = 0# количество необходимых мест
        p = []#предыдущий контейнер
        mav = 0#макс кол-во вложений

        while len(a) > 0 and len(b) > 0:#пока что-то не закончилось
            if ka == len(a) or kb == len(b):#если не удалось вложить ни один конт. значит вложения закончились. нужна новая цепь
                kol+=1
                mav = max(mav, v)
                p = []
                ka = 0
                kb = 0
                v = 0
            if p == []:#начало цепи. нет предыдущего конт.
                if a[ka]-7 >= b[kb]:#если могу вложить в конт а конт б
                    v+=1#увеличиваю вложенные
                    a = a[:ka] + a[ka+1:]
                    p = [b[kb], "b"]#предыдущий конт
                    b = b[:kb] + b[kb+1:]#удаляю использованный конт.
                elif b[kb] - 7 >= a[ka]:#если могу вложить в конт б конт а
                    v+=1
                    b = b[:kb] + b[kb+1:]
                    p = [a[ka], "a"]
                    a = a[:ka] + a[ka + 1:]
                else:#не получилось вложить
                    if a[ka] > b[kb]:#если конт а больше конт б и не удалось вложить то смотрю на следующий конт б
                        kb +=1
                    else:
                        ka +=1#и наоборот
            else:
                if p[1] == "b":#предыдущий контейнер б
                    if a[ka] <= p[0]-7:#получается вложить контейнер а
                        p = [a[ka], "a"]
                        a = a[:ka] + a[ka+1:]
                        v+=1
                        ka = 0
                    else:#если нет, то смотрю на следующий
                        ka+=1
                else:#предыдущий контейнер а
                    if b[kb] <= p[0] - 7:#получается вложить контейнер б
                        v+=1
                        p = [b[kb], "b"]
                        b = b[:kb] + b[kb+1:]
                        kb = 0
                    else:#если нет, то смотрю на следующий
                        kb +=1
        kol += len(a) + len(b)#те которые не влезли
    print(kol, mav)

def st_3(n):
    for i in range(10, 0, -1):
        if n%(3**i) == 0:
            return i
    return -1

def n27():
    a = 59049#3**10
    b = [[]]*11
    with open("f") as f:
        c = list(map(int, f))
        for i in range(len(b)):
            if i == 0:
                b[i] = list(filter(lambda x: st_3(x) == -1, c))
            else:
                b[i] = list(filter(lambda x: st_3(x) == i, c))
    k  =0
    for i in range(len(b)):
        for y in range(i+1, len(b)):
            if i+y >=10 and b[i] != [] and b[y] != []:
                for x in range(len(b[i])):
                    for z in range(len(b[y])):
                        if (b[i][x] + b[y][z])%4 == 0:
                            k+=1
    print(k)
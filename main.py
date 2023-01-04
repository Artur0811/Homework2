def n21():
    def p(x ,y, h):
        if x+ y >= 81 or h > 5:
            return h == 5
        if h == 4:
            if x < y:
                return p(x + 1, y, h + 1) and p(x + 2, y, h + 1) and p(x * 2, y, h + 1)
            return p(x, y + 1, h + 1) and p(x, y + 2, h + 1) and p(x, y * 2, h + 1)
        if x < y:
            return p(x + 1, y, h + 1) or p(x + 2, y, h + 1) or p(x * 2, y, h + 1)
        return p(x, y + 1, h + 1) or p(x, y + 2, h + 1) or p(x, y * 2, h + 1)


    def f(x, y, h):
        if x + y >= 81 and (h == 5 or h == 3):
            return True
        if x + y >= 81 and (h == 2 or h == 4) or h > 5:
            return False
        if h % 2 == 1:
            if x < y:
                return f(x + 1, y, h + 1) and f(x + 2, y, h + 1) and f(x * 2, y, h + 1)
            return f(x, y + 1, h + 1) and f(x, y + 2, h + 1) and f(x, y * 2, h + 1)
        if x < y:
            return f(x + 1, y, h + 1) or f(x + 2, y, h + 1) or f(x * 2, y, h + 1)
        return f(x, y + 1, h + 1) or f(x, y + 2, h + 1) or f(x, y * 2, h + 1)


    for i in range(1, 69):
        if f(12, i, 1) and p(12, i, 1):
            print(i)

def n24():
    s = 0
    ps = 0
    ka = 0
    with open("24.txt") as f:
        a = f.readline().strip().split("F")
        for i in range(len(a)):
            if a[i].count("A")<=2:
                if i == 0 or i == len(a)-1:
                    ps +=1+len(a[i])
                else:
                    ps += 2 + len(a[i])
                ka += a[i].count("A")
                for y in range(i+1, len(a)):
                    ka += a[y].count("A")
                    if ka > 2:
                        ka = 0
                        s = max(s, ps)
                        ps = 0
                        break
                    else:
                        if y == len(a)-1:
                            ps += len(a[y])
                        else:
                            ps += len(a[y]) + 1
            s = max(s, ps)
            ka = 0
            ps = 0
    print(s)

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
            if i+y >=8 and b[i] != [] and b[y] != []:
                for x in range(len(b[i])):
                    for z in range(len(b[y])):
                        if (b[i][x] + b[y][z])%4 == 0:
                            k+=1
    print(k)

n27()


def n23():
    def f(x, y):
        if x == y:
            return 1
        if x > y:
            return 0
        if x == 12:
            return 0
        return f(x+1, y)+f(x+2, y)+f(x*3, y)
    print(f(2, 9)*f(9, 19))#650

def n24():
    with open("24_demo (1).txt") as f:
        a = f.read()
        k = 0
        ma = 0
        for i in range(len(a)):
            if a[i] == "Y":
                k+=1
            else:
                if ma<k:
                    ma = k
                k = 0
        print(ma)#10

def n25():
    for i in range(201455, 201471):
        m = []
        for y in range(1, round(i**0.5)+1):
            if i%y == 0:
                if i//y == y:
                    m.append(y)
                else:
                    m.append(y)
                    m.append(i//y)
            if len(m) > 4:
                break
        if len(m) == 4:
            print(sorted(m))
            #[1, 3, 67153, 201459]
            #[1, 13, 15497, 201461]
            #[1, 29, 6947, 201463]
            #[1, 2, 100733, 201466]

def n26():
    with open("27886.txt") as f:
        s, n = map(int, f.readline().split())
        a = sorted(map(int, f))
        k, ma = 0, 0
        for i in range(len(a)):
            if s-a[i] > 0:
                k+=1
                s-=a[i]
                ma = a[i]
    ma+=s
    while ma not in a:
        ma -=1
    print(k, ma)#458 39
def n27(name):
    with open(name) as f:
        n = f.readline()
        a = list(map(int, f))
        b = list(filter(lambda x: x%2 == 1, a))
        def f(nech, m):
            if len(nech)%10 == 0:
                return m
            else:
                c = m[::-1]
                r, l = 0, 0
                rk, lk = 0, 0
                for i in range(len(m)):
                    if m[i]%2 == 0:
                        r+=m[i]
                        rk+=1
                    else:
                        r+=m[i]
                        rk+=1
                        break
                for i in range(len(c)):
                    if c[i]%2 == 0:
                        l+=c[i]
                        lk+=1
                    else:
                        l+=c[i]
                        lk+=1
                        break
                if r>=l:
                    return f(nech[:-1], m[:-lk])
                else:
                    return f(nech[1:], m[rk:])
        print(sum(f(b, a)))
n27("27-A.txt")#4767652
n27("27-B.txt")#979268310
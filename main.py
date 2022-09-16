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
        l = len(list(filter(lambda x:x%2 == 1, a)))%10
        summa = sum(a)
        left = []
        k = 0
        for i in range(len(a)):
            k+=a[i]
            if a[i]%2 == 1:
                left.append(k)
                k = 0
                if  len(left) == l:
                    break
        right = []
        for i in range(1, len(a)):
            k+=a[-i]
            if a[-i]%2 == 1:
                right.append(k)
                k = 0
                if len(right) == l:
                    break
        for i in range(l):
            if left[i] > right[i]:
                summa -=right[i]
            else:
                summa-=left[i]
        print(summa)

n27("27-A.txt")#4777208
n27("27-B.txt")#979268310
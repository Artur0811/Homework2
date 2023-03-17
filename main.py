def n24_1():
    with open("f.txt") as f:
        a = f.read().strip()
        s = {}
        for i in range(len(a)-1):
            if a[i] == "E":
                if a[i+1] in s:
                    s[a[i+1]] +=1
                else:
                    s[a[i+1]] = 1
        m = 0
        b = ""
        for i in s:
                if s[i] > m:
                    m = s[i]
                    b = i
    print(b)#Y

def n24_2():
    with open("f.txt") as f:
        a = f.read().strip()
        e = 0
        l = 0
        ma = 0
        for i in range(len(a)):
            if a[i] == "E":
                e+=1
                l+=1
            elif a[i] == "A":
                if e >=3:
                    ma = max(ma, l)
                e = 0
                l = 0
            else:
                l+=1
        print(ma)#282

def n25_1():
    n1 = [str(i) for i in range(10)]
    p1 = [""] +[str(i) for i in range(1000)]
    rez = []
    for i in range(len(n1)):
        for y in range(len(p1)):
            num = int("1"+n1[i]+"2139"+p1[y]+"4")
            if num%2023 == 0:
                rez.append([num, num//2023])
    rez = sorted(rez, key=lambda x: x[0])
    for i in rez:
        print(*i)
        #162139404 80148
        #1321399324 653188
        #1421396214 702618
        #1521393104 752048

def n25_2():
    def f(n):
        k = 0
        for i in range(1, round(n**0.5)+1):
            if n%i == 0:
                if i%2 == 1:
                    k+=1
                if (n//i)%2 == 1:
                    k+=1
            if k > 5:
                break
        return k == 5
    for i in range(35000000, 40000001):
        if f(i):
            print(i)
            #35819648
            #39037448
            #39337984
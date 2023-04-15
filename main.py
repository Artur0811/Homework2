with open("f.txt") as f:
    n = f.readline()
    a = list(map(int, f))
    l, r = 0 , 0
    sl, sr = 0, 0
    if len(a)%2 == 0:
      ser = len(a)//2
    else:
      ser = len(a)//2+1
    for i in range(1, ser):
        r += a[i]
        sr += a[i]*i
    if len(a)%2 == 0:
      ser = len(a)//2
    else:
      ser = len(a)//2
    for i in range(-ser, 0):
        l += a[i]
        sl -= i*a[i]
    mi = sr + sl
    v  = 1
    for i in range(1, len(a)):
        sr -= r
        r -= a[i]
        l += a[i-1]
        sl += l
        if len(a)%2 == 0:
            sr += a[(i+len(a)//2 -1)%len(a)]*(len(a)//2-1)
            r += a[(i+len(a)//2 -1)%len(a)]
            sl -= a[(i+len(a)//2 -1)%len(a)]*(len(a)//2+1)
            l -= a[(i+len(a)//2 -1)%len(a)]
        else:
            sr += a[(i + len(a) // 2)%len(a)] * (len(a) // 2)
            r += a[(i + len(a) // 2)%len(a)]
            sl -= a[(i + len(a) // 2)%len(a)] * (len(a) // 2+1)
            l -= a[(i + len(a) // 2)%len(a)]
        if sr + sl < mi:
            mi = sr + sl
            v = i+1
print(mi)
def n27(name):
    with open(name) as f:
        n = f.readline()
        a= list(map(int, f))
    a = list(map(lambda x:x*3, a))
    sl, sr =0,0
    p=0
    mi =9999999999999999999999999999999999999999999999999999999
    for i in range((len(a)-1)//2):
        p+=1
        sr+=a[p]
        sl+=a[-p]
    if (len(a)-1)%2 == 1:
        p+=1
        sr+=a[p]
    a0l = 0
    a0r = 0
    p=0
    for i in range((len(a)-1)//2):
        p+=1
        a0r+=p*a[p]
        a0l+=p*a[-p]
    if (len(a)-1)%2 == 1:
        p+=1
        a0r+=(p)*a[p]
    for i in range(1,len(a)):
        a0r-=sr
        if i+p < len(a):
            a0r+=p * a[i+p]
            sr+=a[i+p]
        else:
            a0r += p * a[i + p- len(a)]
            sr += a[i + p-len(a)]
        sr-=a[i]
        sl+=a[i-1]
        a0l+=sl
        sl-=a[i-p]
        a0l-=p*a[i-p]
        if a0l+a0r<mi:
            mi = a0l+a0r
            k = i
    return mi
print(n27("107_27_A.txt"))#471228
print(n27("107_27_B.txt"))#49113954961677
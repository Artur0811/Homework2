a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = int(input())

if k+a> 2*k:
    print(k)
elif k + b > 2 * k:
    print(k+a)
elif k+a-c< 0:
    print(a+a+k+b)
elif k+b-d<0:
    print(b+b+k+a+c)
else:
    s = 0
    dx = b-d
    dy = a-c
    m = []
    if dx!=0:
        m+=[(2*k-d)//abs(dx), d//abs(dx)]
    if dy!=0:
        m+=[(2*k-a)//abs(dy), c//abs(dy)]
    col = min(m)-1
    s+=col*(a+b+c+d)
    cor=[k+dx*col, k+dy*col]
    while True:
        if cor[1] + a <= 2*k:
            cor[1] += a
            s+=a
        else:
            s+=2*k-cor[1]
            break
        if cor[0] + b <= 2*k:
            s+=b
            cor[0] += b
        else:
            s+=2*k-cor[0]
            break
        if cor[1] - c >= 0:
            s+=c
            cor[1] -=c
        else:
            s+=cor[1]
            break
        if cor[0] - d >= 0:
            s+=d
            cor[0]-=d
        else:
            s+=cor[0]
            break
    print(s)
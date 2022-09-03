test = [    "",#-1
            "(",#1
            ")",#1
            "((",#-1
            "(()",#1
            "()",#-1
            "(()())()",#-1
            "((()",#-1
            ")(",#-1
            "d + (a + (b + c) = (a + b) + c + d",#5
            "()(()=()",#3
            "() = (()"#6
]

a = "123456"
i = 1

def ud(a, k=1):
    if k == 0:
        return a
    else:
        n = 0
        for i in range(len(a)-1):
            if a[i][0] == "(" and a[i+1][0] == ")":
                a = a[:i] + a[i+2:]
                n+=1
                break
        return ud(a, n)

for a in test:
    k = []
    l, r = 0, 0
    for num, el in enumerate(a, 1):
        if el == "(" or el == ")":
            k.append([el, num])
    a = ud(k)
    if len(a) == 1:
        print(a[0][1])
    else:
        print(-1)

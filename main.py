coins = [1,2,5]
n = 11
res = 3

# coins = [2]
# n = 3
# res = -1
#
# coins = [1]
# n = 0
# res = 0

def f(s, data):
    if s == 0:
        return 0
    if s%data[-1] == 0:
        return s//data[-1]
    m = set(data)
    mi = min(data)
    res = []
    while s > mi:
        res.append(mi)
        s-=mi
        if s in m:
            res.append(s)
            break
    if s not in m:
        return 0
    else:
        res.append(s)
    print(res)
f(n, coins)


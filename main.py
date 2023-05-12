# coins = [1,2,5]
# n = 11
# res = 3

# coins = [2]
# n = 3
# res = -1
#
# coins = [1]
# n = 0
# res = 0
n = 22
coins = [1, 5, 10]
def f(s, data):
    if s == 0:
        return 0
    if s%data[-1] == 0:
        return s//data[-1]
    val = []
    m = set(data)
    for i in m:
        if s- i >=0:
            val.append([s-i, 1])
    if val == []:
        return -1
    res = s
    t = True
    while val != []:
        for i in m:
            if val[0][0] - i > 0:
                val.append([val[0][0]- i, val[0][1]+1])
            elif val[0][0] - i == 0:
                res = min(res, val[0][1]+1)
                t = False
        val = val[1:]
    if t:
        return -1
    return res
print(f(n, coins))
def f(stroka, patern, f_st = "", n= 0, k = 0):
    if len(patern) == k:
        return stroka == f_st
    if patern[k] == ".":
        if len(stroka) == n:
            return False
        return f(stroka, patern, f_st+stroka[n], n+1, k+1)
    if len(patern) -1 > k:
        if patern[k+1] == "*":
            if n != len(stroka):
                if stroka[n] == patern[k]:
                    return f(stroka, patern, f_st+ stroka[n], n+1, k)
            return f(stroka, patern, f_st, n, k+2)
    return f(stroka, patern, f_st + patern[k], n+1,k+1)

print(f("aaaaaaasdfsg", "b*a*....."))


def func(data, p):
    data = sorted(data)
    mi = 99999999
    s = 999999999
    for i in range(len(data)):
        for y in range(i+2, len(data)):
            k = i+1
            while k < y:
                if abs(p - data[i] - data[y] - data[k]) < mi:
                    mi = abs(p - data[i] - data[y] - data[k])
                    s = data[i] + data[y] + data[k]
                k+=1
    return s
#
# print(func([-1, 2, 1, -4], 1))
for i in range(-10, 11):
    print(func([-5, -10,  2, 1, -7], i), i)
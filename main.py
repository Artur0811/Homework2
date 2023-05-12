m = [1, 4, 6, 8, 2, 1, 19, 8,7,3]
m1 = [1, 3, 1, 3, 3, 19, 11]

def f(data):
    if len(data) == 0:
        return 0
    if len(data)<=2:
        return max(data)
    if len(data) == 3:
        return max(data[0] + data[2], data[1])
    data[2] += data[0]
    res = max(data[:3])
    for i in range(3, len(data)):
        if data[i-2] < data[i- 3]:
            if res < data[i] + data[i-3]:
                res = data[i] + data[i-3]
            data[i] += data[i-3]
        else:
            if res < data[i] + data[i-2]:
                res = data[i] + data[i-2]
            data[i] += data[i-2]
    return res
print(f(m1))
m = [[9,9,4],
     [6,6,8],
     [2,1,1]]

def n(data, x, y):
    res = []
    if x-1>=0 and data[y][x-1] > data[y][x]:
        res.append((x-1, y))
    if x+1< len(data[0]) and data[y][x+1] > data[y][x]:
        res.append((x+1, y))
    if y+1< len(data) and data[y+1][x] > data[y][x]:
        res.append((x, y+1))
    if y-1>=0 and data[y-1][x] > data[y][x]:
        res.append((x, y-1))
    return  res

def f(data):
    res = []
    for i in range(len(data)):
        for y in range(len(data[0])):
            var = n(data, y, i)
            if var != []:
                o=[]
                v = [data[i][y]]
                for z in range(len(var)):
                    o.append([v+[data[var[z][1]][var[z][0]]], var[z]])
                while o!= []:
                    a = o[0]
                    b = a[0]
                    o = o[1:]
                    var = n(data, a[1][0], a[1][1])
                    if var == []:
                        res.append(b)
                    else:
                        for z in range(len(var)):
                            o.append([b + [data[var[z][1]][var[z][0]]], var[z]])
    res = max(res, key= lambda x: len(x))
    return res
m1 = [[1, 4, 5, 7],
      [1, 3, 8, 7],
      [0, 4, 6, 9],
      [11, 8, 5, 17],]
print(f(m))
from PIL import Image, ImageDraw

def d(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return (x ** 2 + y ** 2) ** 0.5


def ClosestSplitPair(px, py, dist, best_pair):
    xs = px[len(px) // 2][0]
    Sy = list(filter(lambda x: xs - dist <= x[0] <= xs + dist, py))
    best_d = dist
    best_p = best_pair
    for i in range(len(Sy) - 1):
        for j in range(i + 1, min(i + 7, len(Sy))):
            p, q = Sy[i], Sy[j]
            if d(p, q) < best_d:
                best_p = p, q
                best_d = d(p, q)
    return best_p[0],best_p[1],best_d


def p(data):
    best_d = d(data[0], data[1])
    best_p = data[0], data[1]
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            p, q = data[i], data[j]
            if d(p, q) < best_d:
                best_p = p, q
                best_d = d(p, q)
    return best_p[0],best_p[1],best_d


def ClosestPair(px, py):
    if len(px) <= 3:
        return p(px)
    Qx = px[len(px) // 2:]
    Rx = px[:len(px) // 2]
    Qy = []
    Ry = []
    for i in range(len(py)):
        if px[len(px) // 2][0] <= py[i][0]:
            Qy.append(py[i])
        else:
            Ry.append(py[i])
    p1, q1, d1 = ClosestPair(Qx, Qy)
    p2, q2, d2 = ClosestPair(Rx, Ry)
    dist = min((p1, q1, d1), (p2, q2, d2), key=lambda x: x[2])
    p3, q3, d3 = ClosestSplitPair(px, py, dist[2], (dist[0], dist[1]))
    x, y, z = d(p1, q1), d(p2, q2), d(p3, q3)
    if x < y and x < z:
        return p1, q1, x
    elif y < x and y < z:
        return p2, q2, y
    else:
        return p3, q3, z

def map(m):
    ma_ = 0
    for i in range (len(m)):
        if abs(m[i][0])  > ma_:
            ma_ = abs(m[i][0])
        elif abs(m[i][1])  > ma_:
            ma_ = abs(m[i][1])
    ma_+=20
    x = 1000//ma_
    c = x * ma_
    p = Image.new("RGB", (c * 2, c * 2), (255, 255, 255))
    dr = ImageDraw.Draw(p)
    dr.line(((c, 0),(c, c*2)), width=1, fill=(0,0,0))
    dr.line(((0, c), (c*2, c)), width=1, fill=(0, 0, 0))
    for i in range(len(m)):
        x1,y1, x2, y2 = c+m[i][0]*x-(x//2), c-m[i][1]*x-(x//2), c+m[i][0]*x+(x//2),c-m[i][1]*x+(x//2)
        dr.ellipse(((x1, y1), (x2, y2)),width=1, fill=(0,0,0))
    for i in range(1, ma_-1):
        x0,  x1 = c+i*x,  c-i*x
        dr.line(((x0, c-x), (x0, c +x)), width=1, fill=(0, 0, 0))
        dr.line(((x1, c - x), (x1, c + x)), width=1, fill=(0, 0, 0))
        dr.line(((c - x, x0), (c+x, x0)), width=1, fill=(0, 0, 0))
        dr.line(((c - x, x1), (c + x, x1)), width=1, fill=(0, 0, 0))
    p.save("map.png")

m = [(3, 4), (0, 1),(9, 99),(3, 100),(3, 5),(16, 4),(-5, 4),(-5, -20)]
print(ClosestPair(sorted(m, key=lambda x:x[0]), sorted(m, key=lambda x:x[1])))
m = [(-3, 5), (0, 0),(-21, -7),(-32, 99),(-3, -5),(0, 7),(-65, 4),(-65, -20),(23, 24), (23, 1),(19, 9),(7, -9),(13, 5),(16, -4),(51, -84),(45, 120)]
print(ClosestPair(sorted(m, key=lambda x:x[0]), sorted(m, key=lambda x:x[1])))
m = [(0, 5), (5, 0),(10, 10),(-10, -10),(-23, -25),(20, -17),(-15, -20),(-25, -20),(0, 1), (23, 1),(19, 91),(7, -91),(13, 15),(19, -14),(51, -84),(54, -83),(5-6, 102),(51, 1),(45, 1)]
print(ClosestPair(sorted(m, key=lambda x:x[0]), sorted(m, key=lambda x:x[1])))
map(m)
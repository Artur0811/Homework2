a = []
with open("18_demo.txt") as f:
    for i in f:
        a.append(list(map(int, i.split())))

def f(mas, x = 0, y = 0, s = 0):
    if x >= len(mas[0]):
        return 9999
    if y >= len(mas):
        return 9999
    if x == len(mas[0])-1 and y == len(mas)-1:
        return s+mas[x][y]
    return min(f(mas, x+1, y, s+mas[x][y]), f(mas, x, y+1, s+mas[x][y]))
print(f(a))
print("Тип 19 № 28083")
def f(x, h):
    if h > 3 or x >= 26:
        return h == 3
    return f(x+1, h+1) or f(x*2, h+1)
for i in range(1, 26):
    if f(i, 1):
        print(i)
        break
print("Тип 20 № 28084")
def f1(x, h):
    if h > 4 or x >= 26:
        return h == 4
    if h %2 == 0:
        return f1(x+1, h+1) and f1(x*2, h+1)
    else:
        return f1(x+1, h+1) or f1(x*2, h+1)
for i in range(1, 26):
    if f1(i, 1):
        print(i)
print("Тип 21 № 28085")
def f2(x, h):
    if x>= 26 and (h == 5 or h==3):
        return True
    if h > 5 or (x>= 26 and (h == 2 or h==4)):
        return False
    if h%2 == 1:
        return f2(x+1, h+1) and f2(x*2, h+1)
    return f2(x+1, h+1) or f2(x*2, h+1)
for i in range(1, 26):
    if f2(i, 1):
        print(i)
print("Тип 20 № 27763")
def f4(x, y, h):
    if x+y >= 47 or h > 4:
        return h == 4
    if h %2== 0:
        return f4(x+1, y+2, h+1) and  f4(x+2, y+1, h+1) and  f4(x*2, y, h+1) and  f4(x, y*2, h+1)
    return f4(x+1, y+2, h+1) or f4(x+2, y+1, h+1) or f4(x * 2, y, h + 1) or f4(x, y * 2, h + 1)
ma = 0
for i in range(1, 37):
    if f4(10, i, 1):
        ma = i
print(ma)
print("Тип 21 № 27764")
def f5(x, y, h):
    if x+y >= 47 and (h==5 or h == 3):
        return True
    if (x+y >= 47 and (h==4 or h == 2)) or h > 5:
        return False
    if h%2 == 1:
        return f5(x+1, y+2, h+1) and  f5(x+2, y+1, h+1) and  f5(x*2, y, h+1) and  f5(x, y*2, h+1)
    return f5(x+1, y+2, h+1) or f5(x+2, y+1, h+1) or f5(x * 2, y, h + 1) or f5(x, y * 2, h + 1)
for i in range(1, 36):
    if f5(10, i, 1):
        print(i)
        break
print("Тип 19 № 27777")
def f6(x, y, h):
    if x+y<=40 or h>3:
        return h == 3
    return f6(x-1, y, h+1) or f6(x, y-1, h+1) or f6(x-(x//2), y, h+1) or f6(x, y-(y//2), h+1)
ma= 0
for i in range(21, 100):
    if f6(20, i, 1):
        ma = i
print(ma)
print("Тип 20 № 27778 ")
k = 0
def f7(x, y, h):
    if x+y<= 40 or h>4:
        return h == 4
    if h %2==0:
        return f7(x-1, y, h+1) and f7(x, y-1, h+1) and f7(x-(x//2), y, h+1) and f7(x, y-(y//2), h+1)
    return f7(x - 1, y, h + 1) or f7(x, y - 1, h + 1) or f7(x - (x // 2), y, h + 1) or f7(x, y - (y // 2), h + 1)
for i in range(21, 100):
    if f7(20, i, 1):
        print(i)
        k+=1
    if k == 3:
        break
print("Тип 21 № 27779 ")
def f8(x, y, h):
    if x+y<= 40 and (h == 3 or h == 5):
        return True
    if (x+y<= 40 and (h == 2 or h == 4)) or h > 5:
        return False
    if h%2 == 1:
        return f8(x - 1, y, h + 1) and f8(x, y - 1, h + 1) and f8(x - (x // 2), y, h + 1) and f8(x, y - (y // 2), h + 1)
    return f8(x - 1, y, h + 1) or f8(x, y - 1, h + 1) or f8(x - (x // 2), y, h + 1) or f8(x, y - (y // 2), h + 1)
ma = 0
for i in range(21, 1000):
    if f8(20, i , 1):
        ma = i
print(ma)
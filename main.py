import math

def n27(name):
    with open(name) as f:
        n = f.readline()
        a = list(map(int, f))
        l = len(list(filter(lambda x:x%2 == 1, a)))%10
        summa = sum(a)
        left = []
        k = 0
        for i in range(len(a)):
            k+=a[i]
            if a[i]%2 == 1:
                left.append(k)
                k = 0
                if len(left) == l:
                    break
        right = []
        for i in range(1, len(a)):
            k+=a[-i]
            if a[-i]%2 == 1:
                right.append(k)
                k = 0
                if len(right) == l:
                    break
        msx_sum = 0
        for i in range(l+1):
            if summa-sum(right[i:])-sum(left[:i])>msx_sum:
                msx_sum = summa-sum(right[i:])-sum(left[:i])

        print(msx_sum)
n27("27-A.txt")#4777208
n27("27-B.txt")#979268310

def n27(name):
    with open(name) as f:
        n = f.readline()
        a = []
        for i in f:
            a.append(list(map(int, i.split())))
        a = list(map(lambda x: [x[0],math.ceil(x[1]/36)], a))

        ls, rs = 0, 0
        right, left = 0, 0
        for i in range(1, len(a)):
            rs+=a[i][1]
            right += abs(a[0][0]-a[i][0])* a[i][1]

        mini = right
        for i in range(1, len(a)):
            right-=abs(a[i-1][0]-a[i][0])*rs
            ls +=a[i-1][1]
            left += ls*abs(a[i-1][0]-a[i][0])
            rs -=a[i][1]
            if right+left<mini:
                mini = right+left
        print(mini)
n27("27_A.txt")#51063
n27("27_B.txt")#5634689219329


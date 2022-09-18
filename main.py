import math
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


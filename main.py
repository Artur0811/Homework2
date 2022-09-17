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
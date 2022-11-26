#большое число
def number():
    n = "9"*199090+"0"*10+"1"*900
    k = int(input())
    num = {i:n.count(str(i)) for i in range(10)}
    for i in num:
        a = num[i]
        if k > a:
            k-=a
            n =n.replace(str(i), "")
        else:
            n = n.replace(str(i), "", k)
            break
    print(n)

n = int(input())
m = [int(input()) for i in range(n)]
t = False
for i in range(1, n):
    for y in range(i+1, n):
        a= sorted([sum(m[:i]), sum(m[i:y]), sum(m[y:])])
        if a[1]>0 and a[2] > 0:
            print(i, y-i, n-y)
            t = True
            break
    if t:
        break
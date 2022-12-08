n = int(input())
f = int(input())
if f == 1:
  m= list(map(int, input().split()))
else:
    m1,x,y,z = map(int, input().split())
    c = list(map(int, input().split()))
    m = [0]*n
    for i in range(n):
        if i+1<=m1:
            m[i] = c[i]
        else:
            m[i] = ((x*m[i-2] + y*m[i-1] + z)%(10**9))+1
ix = 0
ma = 0
for i in range(n):
    if m[i]>= ma:
        ma= m[i]
        ix = i
mi = ma
rez = ix
for i in range(ix-1, ix - n, -1):
    if m[i] < m[i+1]:
        m[i]= m[i+1]-1
    if m[i]<= mi:
        mi = m[i]
        if i >= 0:
            rez = i+1
        else:
            rez = n+i+1
print(mi, rez)




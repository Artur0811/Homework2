#27 задача
def n27(name):
    with open(name) as f:
        n = f.readline()
        a= list(map(int, f))
    a = list(map(lambda x:x*3, a))
    sl, sr =0,0
    p=0
    mi =9999999999999999999999999999999999999999999999999999999
    for i in range((len(a)-1)//2):
        p+=1
        sr+=a[p]
        sl+=a[-p]
    if (len(a)-1)%2 == 1:
        p+=1
        sr+=a[p]
    a0l = 0
    a0r = 0
    p=0
    for i in range((len(a)-1)//2):
        p+=1
        a0r+=p*a[p]
        a0l+=p*a[-p]
    if (len(a)-1)%2 == 1:
        p+=1
        a0r+=(p)*a[p]
    for i in range(1,len(a)):
        a0r-=sr
        if i+p < len(a):
            a0r+=p * a[i+p]
            sr+=a[i+p]
        else:
            a0r += p * a[i + p- len(a)]
            sr += a[i + p-len(a)]
        sr-=a[i]
        sl+=a[i-1]
        a0l+=sl
        sl-=a[i-p]
        a0l-=p*a[i-p]
        if a0l+a0r<mi:
            mi = a0l+a0r
            k = i
    return mi
print(n27("107_27_A.txt"))#471228
print(n27("107_27_B.txt"))#49113954961677


#Алгоритм Штрассена
def Pmatrix(x, y):
  m = []
  p1 = x[0][0]*(y[0][1] - y[1][1])
  p2 = (x[0][0]+x[0][1])*y[1][1]
  p3 = (x[1][0]+x[1][1])*y[0][0]
  p4 = (y[1][0]-y[0][0])*x[1][1]
  p5 = (x[0][0]+x[1][1])*(y[0][0]+y[1][1])
  p6 = (x[0][1]-x[1][1])*(y[1][0]+y[1][1])
  p7 = (x[0][0]-x[1][0])*(y[0][0]+y[0][1])
  m.append([p5+p4-p2+p6, p1+p2])
  m.append([p3+p4, p1+p5-p3-p7])
  return m

def Smatrix(x, y):
  for i in range(len(x)):
    for z in range(len(y)):
      x[i][z]+=y[i][z]
  return x

def d(x):
  m1, m2, m3, m4, l = [], [], [], [], len(x[0])
  for i in range(l):
    m2.append(x[i][l // 2:])
    m1.append(x[i][:l // 2])
  m3 = m1[len(m1) // 2:]
  m1 = m1[:len(m1) // 2]
  m4 = m2[len(m2) // 2:]
  m2 = m2[:len(m2) // 2]
  return [m1, m2, m3, m4]

def rek(x ,y):
  if len(x) > 2:
    x = d(x)
    y = d(y)
    return skleyka([Smatrix(rek(x[0], y[0]), rek(x[1], y[2])),  Smatrix(rek(x[0], y[1]), rek(x[1], y[3])),  Smatrix(rek(x[2], y[0]), rek(x[3], y[2])),Smatrix(rek(x[2], y[1]), rek(x[3], y[3]))])
  else:
    return Pmatrix(x, y)

def skleyka(x):
  m = []
  for i in range(len(x[0])):
    m.append(x[0][i] + x[1][i])
  for i in range(len(x[0])):
    m.append(x[2][i] + x[3][i])
  return m

k = [[1, 2, 3, 4],
     [5, 2, 6, 4],
     [1, 7, 9, 8],
     [0, 12, 4, 4]]
b = [[3, 5, 3, 7],
     [8, 112, 23, 4],
     [1, 34, 9, 567],
     [0, 12, 0, 4]]


k = [[1, 0],
     [0,1]]
b = [[1,1],
     [3, 5]]


k = [[2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1]]
b = [[2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1]]
r = rek(k,b)
for i in r:
  print(i)

#№26
with open ("26 (1).txt") as f :
    n = f.readline()
    a = []
    for i in f:
        a.append(list(map(int, i.split())))
r = []
s = 0
for i in range(len(a)):
    if a[i][0]<=1634515200 and a[i][1]>1634515200 or a[i][0]<=1634515200 and a[i][1]==0:
        s+=1
    if 1634515200 < a[i][0]< 1634515200+7*24*3600:
        r.append([a[i][0], 0])
    if 1634515200 < a[i][1]< 1634515200+7*24*3600:
        r.append([a[i][1], 1])
r=sorted(r, key=lambda x:x[0])
sm = s
t = 0
for i in range(len(r)):
    if r[i][1] == 0:
        s+=1
        tn = r[i][0]
    else:
        s-=1
    if sm < s:
        sm = s
        if i+1 != len(r):
            if r[i+1][1] == 1:
                t= r[i+1][0] - tn
        else:
            t = 1634515200+7*24*3600-tn
print(sm, t)

#перемножение матриц
def Pmatrix(x, y):
  m = [[0 for i in range(len(x))] for i in range(len(x))]
  for i in range(len(x)):
    for z in range(len(y)):
      for h in range(len(y)):
        m[i][z] += x[i][h]*y[h][z]
  return m

def Smatrix(x, y):
  for i in range(len(x)):
    for z in range(len(y)):
      x[i][z]+=y[i][z]
  return x

def d(x):
  m1, m2, m3, m4, l = [], [], [], [], len(x[0])
  for i in range(l):
    m2.append(x[i][l // 2:])
    m1.append(x[i][:l // 2])
  m3 = m1[len(m1) // 2:]
  m1 = m1[:len(m1) // 2]
  m4 = m2[len(m2) // 2:]
  m2 = m2[:len(m2) // 2]
  return [m1, m2, m3, m4]

def rek(x ,y):
  if len(x) > 2:
    x = d(x)
    y = d(y)
    return skleyka([Smatrix(rek(x[0], y[0]), rek(x[1], y[2])),  Smatrix(rek(x[0], y[1]), rek(x[1], y[3])),  Smatrix(rek(x[2], y[0]), rek(x[3], y[2])),Smatrix(rek(x[2], y[1]), rek(x[3], y[3]))])
  else:
    return Pmatrix(x, y)

def skleyka(x):
  m = []
  for i in range(len(x[0])):
    m.append(x[0][i] + x[1][i])
  for i in range(len(x[0])):
    m.append(x[2][i] + x[3][i])
  return m

k = [[1, 2, 3, 4],
     [5, 2, 6, 4],
     [1, 7, 9, 8],
     [0, 12, 4, 4]]
b = [[3, 5, 3, 7],
     [8, 112, 23, 4],
     [1, 34, 9, 567],
     [0, 12, 0, 4]]


k = [[1, 0],
     [0,1]]
b = [[1,1],
     [3, 5]]


k = [[2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1]]
b = [[2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [2, 2, 2, 2, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 1, 1]]
r = rek(k,b)
for i in r:
  print(i)
p = Pmatrix(k,b)
for i in p:
  print(i)
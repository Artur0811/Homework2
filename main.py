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
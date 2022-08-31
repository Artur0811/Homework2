def schet(vvod):
    def sum(a, b):
      return a[1]+b[1]

    def delenie(m, k = 0):
      if len(m)>1:
        a = delenie(m[:len(m)//2], k)
        b = delenie(m[len(m)//2:], k)
        k+=a[1]
        k+=b[1]
        c = sliyanie(a[0], b[0], k)
        return c[0], c[1]
      else:
        return m, k


    def sliyanie(a, b, k = 0):
      m = []
      while len(a)> 0 and len(b)>0:
        if a[0] > b[0]:
          k+= len(a)
          m.append(b[0])
          b = b[1:]
        else:
          m.append(a[0])
          a = a[1:]
      m+=a
      m+=b
      return m, k
    return delenie(vvod)
print(schet([9,8, 1,2,3,4]))

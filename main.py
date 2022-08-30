def n4():
    a = "АБВДЕИН"
    b = {"110":"А", "01":"Б", "000":"И"}
    slovo = "ВВЕДЕНИЕ"

    def derevo(l, m,k =0, s={}):
        a= "0"
        b = "1"
        if s == {}:
            for i in m:
                if i == a:
                    s[i] = a
            if a not in s:
                s[a] = {}
            if b not in s:
                s[b] = {}
            return derevo(l,m,  k+1, s)
        if l > k:
            for i in s:
                f = False
                for y in m:
                    if y[:len(i)] == i:
                        f = True
                if f:
                    if s[i] == {}:
                        for y in m:
                            if i+a == y:
                                s[i][i+a] = m[y]
                            if i + b == y:
                                s[i][i + b] = m[y]
                        if i + a not in s[i]:
                            s[i][i + a] = {}
                        if i + b not in s[i]:
                            s[i][i + b] = {}
                        s[i] = derevo(l,m,  k+1, s[i])
            return s
        else:
            return s

    def cod(a, m = {}):
        for i in a:
            if len(a[i]) == 1 or a[i] == {}:
                m[i] = a[i]
            else:
                cod(a[i], m)
        return m

    def dlina(s, bukvi, stroka, best = 99999):
        if len(s) == len(bukvi):
            m, n = [], list(bukvi)
            for i in s:
                if s[i] == {}:
                    m.append(i)
                else:
                    n.remove(s[i])
            m = sorted(m, key=lambda x:len(x))
            n = sorted(n, key=lambda x:stroka.count(x))[::-1]
            for i in range (len(m)):
                s[m[i]] = n[i]
            k = 0
            for i in range(len(stroka)):
                for y in s:
                    if s[y] == stroka[i]:
                        k+=len(y)
            return k
        else:
            for i in s:
                m = {}
                if s[i] == {}:
                    for y in s:
                        if y != i:
                            m[y] = s[y]
                    m[i+"1"] = {}
                    m[i+"0"] = {}
                    c = dlina(m, bukvi, stroka)
                    if c < best:
                        best = c
        return best


    def fano(s):
        l = 1
        for i in s:
            if len(i)>l:
                l = len(i)
        d = derevo(l, b)
        s = cod(d)
        dl = dlina(s, a, slovo)
        print(dl)

    fano(b)

n4()

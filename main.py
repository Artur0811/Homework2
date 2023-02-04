with open("17.txt") as f:
    n = f.readline()
    s = 0
    ch, nch = 0 , 0
    ra1 = [999999,9999999]
    ra2 = [999999,9999999]
    for i in f:
        a = list(map(int, i.split()))
        if a[0] > a[1]:
            if a[0]%2 == 0:
                 ch +=1
                 if a[1]%2 == 1:
                     ra1.append(a[0] - a[1])
                     ra1 = sorted(ra1)[:2]
            else:
                if a[1]%2 == 0:
                    ra2.append(a[0] - a[1])
                    ra2 = sorted(ra2)[:2]
                nch +=1
            s+=a[0]
        else:
            if a[1] % 2 == 0:
                ch += 1
                if a[0]%2 == 1:
                    ra1.append(a[1] - a[0])
                    ra1 = sorted(ra1)[:2]
            else:
                if a[0]%2 == 0:
                    ra2.append(a[1] - a[0])
                    ra2 = sorted(ra2)[:2]
                nch += 1
            s += a[1]
    if s%2 == 0 and ch > nch or s%2 == 1 and nch > ch:
        print(s)
    else:
        if abs(ch - nch) == 1:
            print(ra1, ra2, s, "22")
            m = []
            if nch > ch:
                m.append(s-ra1[0])
                m.append(s - ra2[0]- ra2[1])
            else:
                m.append(s - ra2[0])
                m.append(s - ra1[0] - ra1[1])
            print(max(m))
        else:
            print(max(s-ra2[0] ,s - ra1[0]))




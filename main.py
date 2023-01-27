a = {"A":[["B", 3], ["C", 5], ["D", 11]],
     "B": [["A", 3], ["C", 8], ["D", 5]],
     "C": [["A", 5], ["B", 8]],
     "D" : [["A", 11], ["B", 5]]}

def o_gr(graf, max_t, x,  t_n= 0, past = [], ob_p = []):#сам граф - graf\ лимит по времени - max_t\ начало графа - x
    #время на путь - t_n \пройденый путь на данный момент - past\ обязательные точки - ob_p
    if t_n > max_t:
        return -1
    if past == []:
        roud = []
        v = graf[x]
        past.append(x)
        for i in range(len(v)):
            if v[i][0] not in past:
                a = o_gr(graf, max_t, x, t_n+v[i][1], past+[v[i][0]], ob_p)
                if a != -1:
                    roud += [*a]
        return sorted(roud, key= lambda x:len(list(set(x[0]))))[::-1]
    else:
        pu = []
        v = graf[past[-1]]
        t = True
        for i in range(len(ob_p)):
            if ob_p[i] not in past:
                t = False
        if t:
            pu.append([past, t_n])
        for i in range(len(v)):
            if v[i][0] not in past:
                a = o_gr(graf, max_t, x, t_n + v[i][1], past+ [v[i][0]], ob_p)
                if a != -1:
                    pu+=[*a]
        if pu == []:
            return -1
        return pu

print(o_gr(a, 11, "A"))


class derevo:
    def __init__(self):
        self.item = []
        self.kol = 0
    def ad(self, it, num = 0, k = []):
        if num == 0:
            self.kol+=1
            self.ad(it, num+1, self.item)
        else:
            if num == len(it):
                t = True
                for i in range(len(k)):
                    if k[i]["name"] == it[:num]:
                        k[i]["num"] = k[i]["num"]+[self.kol]
                        t = False
                        break
                if t:
                    k.append({"name": it[:num], "items":[], "num":[self.kol]})
                return k
            else:
                t = True
                for i in range(len(k)):
                    if k[i]["name"] == it[:num]:
                        k[i]["items"] = self.ad(it, num+1, k[i]["items"])
                        k[i]["num"] = k[i]["num"]+[self.kol]
                        t = False
                        break
                if t:
                    k.append({"name": it[:num], "items": self.ad(it, num+1, []), "num": []})
                return k

    def fiend(self, it, num = 0, k = []):
        if num == 0:
            return self.fiend(it, num+1, self.item)
        else:
            if len(it) == num:
                for i in range(len(k)):
                    if k[i]["name"] == it:
                        if k[i]["num"] == []:
                            return -1
                        return max(k[i]["num"])
                return -1
            for i in range(len(k)):
                if k[i]["name"] == it[:num]:
                    return self.fiend(it, num+1, k[i]["items"])

d = derevo()
n, q = map(int, input().split())
while n > 0:
    d.ad(input())
    n-=1
a = []
while q > 0:
    a.append(input().split()[1])
    q-=1
for i in range(len(a)):
    print(d.fiend(a[i]))
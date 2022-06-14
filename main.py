from pymorphy2 import MorphAnalyzer
a, m = "1", []
while a != "":
    a = input()
    if a != "":
        m+=a.split()
rez_s, rez_n = [], []
for i in range(len(m)):
    if "," in m[i] or "." in m[i] or "!" in m[i]:
        m[i] = m[i][:-1]
    a = MorphAnalyzer().parse(m[i])[0]
    if a.tag.POS == "VERB" or a.tag.POS == "INFN":
        if "impf" in a.tag:
            rez_n.append(a.normal_form)
        else:
            rez_s.append(a.normal_form)
rez = sorted(list(set(rez_n))) + sorted(list(set(rez_s)))
for i in rez:
    print(i)
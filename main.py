from pymorphy2 import MorphAnalyzer
a  = "1"
m = []
while a != "":
    a = input()
    if a != "":
        m.append(a.split(" "))
    else:
        break

for i in range(len(m)):
    if MorphAnalyzer().parse(m[i][0])[0].tag.POS == "NOUN":
        w = MorphAnalyzer().parse(m[i][1])[0]
        s = MorphAnalyzer().parse(m[i][0])[0]
        a = m[i][0]
        m[i][0], m[i][1] = m[i][1], a
    else:
        s = MorphAnalyzer().parse(m[i][1])[0]
        w = MorphAnalyzer().parse(m[i][0])[0]
    w = w.inflect({s.tag.gender})
    w = w.inflect({s.tag.case, s.tag.number})
    print(w.word+ " "+ m[i][1])


# глаголы
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

    
# сущ. + прил.
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


# функция human
from PIL import Image,ImageDraw
def human(colf, colline, m, width):
    x, y = m[0], m[1]
    img = Image.new("RGB", (x*16, y*21), colf)
    dr = ImageDraw.Draw(img)
    dr.line(((5 * x, 20 * y), (7 * x, 20 * y)), width=width, fill=colline)
    dr.line(((5 * x, 20 * y), (6 * x, 15 * y)), width=width, fill=colline)
    dr.line(((8 * x, 11 * y), (6 * x, 15 * y)), width=width, fill=colline)
    dr.line(((8 * x, 11 * y), (11 * x, 10 * y)), width=width, fill=colline)
    dr.line(((11 * x, 10 * y), (13 * x, 15 * y)), width=width, fill=colline)
    dr.line(((13 * x, 15 * y), (15 * x, 14 * y)), width=width, fill=colline)
    dr.line(((8 * x, 11 * y), (8 * x, 5 * y)), width=width, fill=colline)
    dr.line(((7 * x, 6 * y), (9 * x, 6 * y)), width=width, fill=colline)
    dr.line(((9 * x, 6 * y), (12 * x, 10 * y)), width=width, fill=colline)
    dr.line(((12 * x, 10 * y), (15 * x, 7 * y)), width=width, fill=colline)
    dr.line(((7 * x, 6 * y), (4 * x, 10 * y)), width=width, fill=colline)
    dr.line(((4 * x, 10 * y), (6 * x, 13 * y)), width=width, fill=colline)
    dr.ellipse(((5 * x - int(x * 0.2), 20 * y - int(x * 0.2)), (5 * x + int(x * 0.2), 20 * y + int(x * 0.2))),width=width, outline=colline)
    dr.ellipse(((6 * x - int(x * 0.2), 15 * y - int(x * 0.2)), (6 * x + int(x * 0.2), 15 * y + int(x * 0.2))),width=width, outline=colline)
    dr.ellipse(((4 * x - int(x * 0.2), 10 * y - int(x * 0.2)), (4 * x + int(x * 0.2), 10 * y + int(x * 0.2))),width=width, outline=colline)
    dr.ellipse(((8 * x - int(x * 0.2), 11 * y - int(x * 0.2)), (8 * x + int(x * 0.2), 11 * y + int(x * 0.2))),width=width, outline=colline)
    dr.ellipse(((7 * x - int(x * 0.2), 6 * y - int(x * 0.2)), (7 * x + int(x * 0.2), 6 * y + int(x * 0.2))),width=width, outline=colline)
    dr.ellipse(((9 * x - int(x * 0.2), 6 * y - int(x * 0.2)), (9 * x + int(x * 0.2), 6 * y + int(x * 0.2))),width=width, outline=colline)
    dr.ellipse(((12 * x - int(x * 0.2), 10 * y - int(x * 0.2)), (12 * x + int(x * 0.2), 10 * y + int(x * 0.2))),width=width, outline=colline)
    dr.ellipse(((11 * x - int(x * 0.2), 10 * y - int(x * 0.2)), (11 * x + int(x * 0.2), 10 * y + int(x * 0.2))),width=width, outline=colline)
    dr.ellipse(((13 * x - int(x * 0.2), 15 * y - int(x * 0.2)), (13 * x + int(x * 0.2), 15 * y + int(x * 0.2))),width=width, outline=colline)
    dr.ellipse(((int(6.5*x), int(1.5*y)), (int(9.5*x), int(4.5*y))),width=width, outline=colline)
    dr.polygon(((6*x, y), (6*x, int(4.5*y)), (8*x, int(2.5*y)), (10*x, int(4.5*y)), (10*x, y)), fill=colf)
    dr.ellipse(((int(6 * x), int(1 * y)), (int(10 * x), int(5 * y))), width=width, outline=colline)
    dr.ellipse(((7 * x - int(x * 0.2), 3 * y - int(x * 0.2)), (7 * x + int(x * 0.2), 3 * y + int(x * 0.2))),width=width, fill=colline)
    dr.ellipse(((9 * x - int(x * 0.2), 3 * y - int(x * 0.2)), (9 * x + int(x * 0.2), 3 * y + int(x * 0.2))),width=width, fill=colline)
    img.save("human.png")
human((255, 255, 255), (0,0,0),(20, 20), 3)


#функция russian_noun
from pymorphy2 import MorphAnalyzer
def russian_noun(word, case = "nomn", number = "sing"):
    w = MorphAnalyzer().parse(word)[0].inflect({case, number}).word
    return w
for case in ["nomn",'gent','datv','accs','ablt','loct','voct']:
    print(russian_noun("свечки", case=case))
print("------------------")
for case in ["nomn",'gent','datv','accs','ablt','loct','voct']:
    print(russian_noun("свечки", case=case, number="plur"))
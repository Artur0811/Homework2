from pymorphy2 import MorphAnalyzer
def russian_noun(word, case = "nomn", number = "sing"):
    w = MorphAnalyzer().parse(word)[0].inflect({case, number}).word
    return w
for case in ["nomn",'gent','datv','accs','ablt','loct','voct']:
    print(russian_noun("свечки", case=case))
print("------------------")
for case in ["nomn",'gent','datv','accs','ablt','loct','voct']:
    print(russian_noun("свечки", case=case, number="plur"))
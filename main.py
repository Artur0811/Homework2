from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
import random

def name(le):
    ast = random.choice(ascii_lowercase + ascii_uppercase)
    if le == 4:
        a = 1
        b = 1
    else:
        a = random.randrange(1, le-2)
        b = le-a-3

    c = False
    while True:
        m = random.choices(''.join(ascii_letters) + ''.join(digits), k=a)

        for i in range(len(digits)):
            if digits[i] in m:
                c = True
                break
        if c:
            break
    ast += "".join(m)
    ast += " "
    ast += random.choice(ascii_uppercase[:len(ascii_uppercase) // 2])
    ast += "".join(random.choices(ascii_lowercase, k=b))
    return ast

def little_green_men_names(m,n):
    rez = []
    while len(rez)!= m:
        a = name(n)
        if a not in rez:
            rez.append(a)
    return rez

print(*little_green_men_names(10, 12), sep="\n")

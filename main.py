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

    while a > 0:
        m = random.choice(''.join(ascii_letters) + ''.join(digits))
        if m not in ast:
            a-=1
            ast+=m
    ast += " "
    while True:
        a = random.choice(ascii_uppercase[:len(ascii_uppercase) // 2])
        if a not in ast:
            ast+=a
            break
    while b > 0:
        m = random.choice(''.join(ascii_letters) + ''.join(digits))
        if m not in ast:
            b-=1
            ast+=m
    return ast

def little_green_men_names(m,n):
    rez = []
    while len(rez)!= m:
        a = name(n)
        if a not in rez:
            rez.append(a)
    return rez

print(*little_green_men_names(10, 12), sep="\n")
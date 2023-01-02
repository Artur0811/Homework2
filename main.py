# def f(x, y, h):
#     if x + y >= 81 and (h == 5 or h == 3):
#         return True
#     if x + y >= 81 and (h == 2 or h == 4) or h > 5:
#         return False
#     if h % 2 == 1:
#         if x < y:
#             return f(x + 1, y, h + 1) and f(x + 2, y, h + 1) and f(x * 2, y, h + 1)
#         return f(x, y + 1, h + 1) and f(x, y + 2, h + 1) and f(x, y * 2, h + 1)
#     if x < y:
#         return f(x + 1, y, h + 1) or f(x + 2, y, h + 1) or f(x * 2, y, h + 1)
#     return f(x, y + 1, h + 1) or f(x, y + 2, h + 1) or f(x, y * 2, h + 1)


def p(x ,y, h):
    if x+ y >= 81 or h > 5:
        return h == 5
    if h == 4:
        if x < y:
            return p(x + 1, y, h + 1) and p(x + 2, y, h + 1) and p(x * 2, y, h + 1)
        return p(x, y + 1, h + 1) and p(x, y + 2, h + 1) and p(x, y * 2, h + 1)
    if x < y:
        return p(x + 1, y, h + 1) or p(x + 2, y, h + 1) or p(x * 2, y, h + 1)
    return p(x, y + 1, h + 1) or p(x, y + 2, h + 1) or p(x, y * 2, h + 1)


def f(x, y, h):
    if x + y >= 81 and (h == 5 or h == 3):
        return True
    if x + y >= 81 and (h == 2 or h == 4) or h > 5:
        return False
    if h % 2 == 1:
        if x < y:
            return f(x + 1, y, h + 1) and f(x + 2, y, h + 1) and f(x * 2, y, h + 1)
        return f(x, y + 1, h + 1) and f(x, y + 2, h + 1) and f(x, y * 2, h + 1)
    if x < y:
        return f(x + 1, y, h + 1) or f(x + 2, y, h + 1) or f(x * 2, y, h + 1)
    return f(x, y + 1, h + 1) or f(x, y + 2, h + 1) or f(x, y * 2, h + 1)


for i in range(1, 69):
    if f(12, i, 1) and p(12, i, 1):
        print(i)

print(p(12, 49, 1))

# with open("22.txt") as f:
#     s = {}
#     for i in f:
#         if "ID" not in i:
#             a = i.split()
#             b = {"time": int(a[1]), "z": a[2].strip('"').split(";"), "end" : 0}
#             s[a[0]] = b
#     for i in s:
#         a = s[i]
#         if a["z"][0] == "0":
#             a["end"] = a["time"]
#         elif len(a["z"]) == 1:
#             a["end"] = a["time"] + s[a["z"][0]]["end"]
#         else:
#             a["end"] = a["time"] + max(s[a["z"][0]]["end"],s[a["z"][1]]["end"])
# k = 0
# for i in s:
#     if s[i]["end"] <=170:
#         k+=1
# print(k)


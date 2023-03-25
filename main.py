a = [
    {
        'id': 123,
        'form': [[1, 0],
                 [1, 1]]
    },
    {
        'id': 231,
        'form': [[1, 1],
                 [0, 1]]
    },
]

res = [
    {
        'id': 123,
        'pos': 1,
        'reverse': True
    }
]

blocks = [
    {
        "id": 443,
        "form": [
            [1, 0, 1],
            [1, 1, 1]
        ]
    },
    {
        "id": 327,
        "form": [
            [0, 1, 0],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 0],
            [0, 1, 0]
        ]
    },
    {
        "id": 891,
        "form": [
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    },
    {
        "id": 4431,
        "form": [
            [1, 0, 1],
            [1, 1, 1]
        ]
    },
    {
        "id": 3271,
        "form": [
            [0, 1, 0],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 0],
            [0, 1, 0]
        ]
    },
    {
        "id": 8911,
        "form": [
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    }
]

res = [
    {
        'id': 443,
        'pos': 1,
        'reverse': False
    },
    {
        'id': 327,
        'pos': 2,
        'reverse': True
    },
    {
        'id': 891,
        'pos': 3,
        'reverse': True
    }
]

bl = [
    {
        "id": 991,
        "form": [
            [0, 0, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
    },
    {
        "id": 443,
        "form": [
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    },
    {
        "id": 327,
        "form": [
            [0, 1, 0],
            [1, 1, 1],
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0]
        ]
    },
    {
        "id": 891,
        "form": [
            [1, 0, 1],
            [1, 1, 1],
            [1, 1, 0]
        ]
    }
]

def connection(block, pat):
    for i in range(len(pat)+1):
        if i == len(pat):
            if i < len(block):
                if 0 in block[i]:
                    return False
        else:
            if pat[i] != block[i]:
                return False
    return True

def tetris(blocks, res = [], start = False, end = False, pat = []):
    if len(blocks) == 0:
        return res
    if start:
        for i in range(len(blocks)):
            b = blocks[i]
            f = b["form"]
            revers = False
            if 0 not in f[-1]:
                revers = True
                f = f[::-1]
            if 0 not in f[0]:
                p = []
                res.append({"id": b["id"], "pos": len(blocks), "revers":revers})
                for y in range(len(f)):
                    if 0 in f[y]:
                        a = []
                        for z in range(len(f[y])):
                            if f[y][z] == 0:
                                a.append(1)
                            else:
                                a.append(0)
                        p.append(a)
                blocks = blocks[:i] + blocks[i+1:]
                return tetris(blocks, res, pat = p)
    else:
        for i in range(len(blocks)):
            b = blocks[i]
            f = b["form"]
            if connection(f, pat):
                f = f[len(pat)+1:]
                p = []
                for y in range(len(f)):
                    if 0 in f[y]:
                        a = []
                        for z in range(len(f[y])):
                            if f[y][z] == 0:
                                a.append(1)
                            else:
                                a.append(0)
                        p.append(a)
                res.append({"id": b["id"], "pos": len(blocks), "revers": False})
                blocks = blocks[:i] + blocks[i+1:]
                return tetris(blocks, res, pat = p)
            elif connection(f[::-1], pat):
                f = f[::-1][len(pat) + 1:]
                p = []
                for y in range(len(f)):
                    if 0 in f[y]:
                        a = []
                        for z in range(len(f[y])):
                            if f[y][z] == 0:
                                a.append(1)
                            else:
                                a.append(0)
                        p.append(a)
                res.append({"id": b["id"], "pos": len(blocks), "revers": True})
                blocks = blocks[:i] + blocks[i + 1:]
                return tetris(blocks, res, pat=p)
        return [{"id": -1, "pos": -1, "revers": -1}]

t = tetris(bl, start=True)
for i in t:
    print(i)
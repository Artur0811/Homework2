class Fifo:
    def __init__(self):
        self.len = 0
        self.items = []
    def add_item(self, other):
        self.len+=1
        self.items.append(other)
    def __getitem__(self, item):
        return self.items[item]
    def __len__(self):
        return self.len
    def empty(self):
        self.items = []
        self.len = 0
    def empty_try(self):
        return self.len == 0

class Lifo:
    def __init__(self):
        self.len = 0
        self.items = []
    def add_item(self, other):
        self.len+=1
        self.items=[other]+self.items
    def __getitem__(self, item):
        return self.items[item]
    def __len__(self):
        return self.len
    def empty(self):
        self.items = []
        self.len = 0
    def empty_try(self):
        return self.len == 0

fi = Fifo()
li =Lifo()
for i in range(10):
    fi.add_item(i)
    li.add_item(i)
print(*fi, "|", *li, sep=" ")
print(len(li), len(fi))
print(li[8], fi[8])
print(li.empty_try())
li.empty()
print(li.empty_try())
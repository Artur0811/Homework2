class obj:
    def __init__(self, item):
        self.item = item
        self.next = None

class Fifo:
    def __init__(self):
        self.head = None
        self.len = 0
    def add_el(self, item):
        self.len+=1
        if self.head == None:
            self.head = obj(item)
        else:
            k = self.head
            while k.next != None:
                k=k.next
            k.next = obj(item)
        return
    def get_el(self):
        if self.head != None:
            return self.head.item
        else:
            return None
    def size(self):
        return self.len
    def empty_try(self):
        return self.head == None
    def empty(self):
        self.head =None

class Lifo:
    def __init__(self):
        self.head = None
        self.len = 0
    def add_el(self, item):
        self.len+=1
        if self.head == None:
            self.head = obj(item)
        else:
            k = obj(item)
            k.next = self.head
            self.head = k
        return
    def get_el(self):
        if self.head == None:
            return None
        else:
            return self.head.item
    def size(self):
        return self.len
    def empty_try(self):
        return self.head == None
    def empty(self):
        self.head =None

f = Fifo()
print(f.empty_try())
for i in range(1, 10):
    f.add_el(i)
print(f.get_el())
print(f.size())
print(f.empty_try())
f.empty()
print(f.empty_try())
print("----------------------------")
l = Lifo()
print(l.empty_try())
for i in range(1, 10):
    l.add_el(i)
print(l.get_el())
print(l.size())
print(l.empty_try())
l.empty()
print(l.empty_try())
class node:
    def __init__(self, value: 0, next: None, prev: None):
        self.val = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None 
        self.capacity = capacity
        self.size = 0
        self.hm = {}
            

    def get(self, key: int) -> int:
        if key in self.hm:
            nod = self.hm[key][1]

            if nod.next:
                if nod.prev:
                    nod.prev.next = nod.next
                    nod.next.prev = nod.prev
                else:
                    nod.next.prev = None
                    self.head = nod.next
                nod.next = None
                self.tail.next = nod
                nod.prev = self.tail
                self.tail = nod  
            return self.hm[key][0]
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if self.size == 0:
            self.head = node(key, None, None)
            self.tail = self.head
            self.size += 1
        elif key in self.hm:
            nod = self.hm[key][1]

            if nod.next:
                if nod.prev:
                    nod.prev.next = nod.next
                    nod.next.prev = nod.prev
                else:
                    nod.next.prev = None
                    self.head = nod.next
                nod.next = None
                self.tail.next = nod
                nod.prev = self.tail
                self.tail = nod
        else:
            if self.size == self.capacity:
                del self.hm[self.head.val]
                self.size -= 1
                if self.head.next:
                    temp = self.head.next
                    self.head.next = None
                    self.head = temp
                    temp.prev = None
            self.tail.next = node(key, None, self.tail)
            self.tail = self.tail.next
            self.size += 1
        self.hm[key] = [value, self.tail]

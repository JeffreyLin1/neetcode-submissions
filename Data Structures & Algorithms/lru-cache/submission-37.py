class node:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.front = None
        self.back = None

    def get(self, key: int) -> int:
        print("getting ", key)
        if key not in self.cache:
            return -1
        curr = self.cache[key]
        if curr == self.front:
            return curr.val
        self.front.next = curr
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        if self.back == curr:
            self.back = curr.next
        curr.next = None       
        curr.prev = self.front
        self.front = curr
        print('back ',self.back.key)
        print('front', self.front.key)
        return curr.val

    def put(self, key: int, value: int) -> None:
        print("putting ", key)
        
        if key in self.cache:
            curr = self.cache[key]
            curr.val = value
            if curr == self.front:
                return
            self.front.next = curr
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            if self.back == curr:
                self.back = curr.next
            curr.next = None       
            curr.prev = self.front
            self.front = curr
            return
        curr = node(key, value)

        self.cache[key] = curr
        if self.front:
            self.front.next = curr
            curr.prev = self.front
        self.front = curr
        
        if not self.back:
            self.back = curr
        self.size += 1
        if self.size > self.capacity:
            self.cache.pop(self.back.key, None)
            self.back = self.back.next
            self.back.prev = None
            self.size -= 1
        print('back ',self.back.key)
        print('front', self.front.key)
        print(list(self.cache.keys()))
            
        
        
        
        
                



        

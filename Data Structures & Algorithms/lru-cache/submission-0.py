class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.cache    = {}

        # Left is LRU, Right is MRU
        self.left = self.right = Node()
        self.left.nxt, self.right.prev = self.right, self.left

    
    def remove(self, node:Node) -> None:
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
  

    def insert_tail(self, node:Node) -> None:
        prev, nxt = self.right.prev, self.right
        node.prev, node.nxt = prev, nxt
        prev.nxt = nxt.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_tail(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert_tail(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]



        

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node(0, 0) # dummy head
        self.tail = Node(0, 0) # dummy tail
        self.head.next = self.tail # connect head to tail
        self.tail.prev = self.head # connect tail to head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.map:
            self.remove(self.map[key]) # remove from current spot
            self.insert(self.map[key]) # move to front
            return self.map[key].val
        return -1
    
    def put(self, key, val):
        if key in self.map:
            self.remove(self.map[key])
        
        node = Node(key, val)
        self.map[key] = node
        self.insert(node)                # insert at front

        if len(self.map) > self.capacity:
            lru = self.tail.prev         # least recent
            self.remove(lru)             # remove from DLL
            del self.map[lru.key]        # remove from hashmap


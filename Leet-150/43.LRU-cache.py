class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache(object):
    def __init__(self, capacity):
       self.capacity = capacity
       self.cache = {}
       self.left = self.right = Node(0,0)
       self.left.next = self.right
       self.right.prev = self.left
        
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        new = Node(key, value)
        self.cache[key] = new
        self.insert(new)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    


# Explanation
# Double Link list
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        # for caching pointers to the Nodes
        self.cache = {}
        
        # Left Node: Least Recently Used (LRU)
        # Right Node: Most Recently Used ()
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
            
    def remove(self, node):
        # removing current node from the chain by linking:
        # previous node's next pointer to the next node
        # next node's previous pointer to the previous node
        
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node):
        # Always inserting on the right
        
        # Adding the node before the right most node
        # Make the connection for prev and next node
        # Add prev, and next to the current node

        prev, next = self.right.prev, self.right
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        # If the key exist we just remove the node
        if key in self.cache:
            self.remove(self.cache[key])
        # else create and insert the node
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # Has to check for capacity and remove the LEAST used Node
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            # lru.key <= important to use the key instead of the node
            del self.cache[lru.key]
            
            
#need to create double linked list
class Node:
    def __init__(self, key,val):
        self.key,self.val = key,val
        self.prev = self.next = None
class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {} #map key to node
        
        #left: LRU and Right is most recent
        self.left,self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
     
    #add to to the right side, after the prev node and before the right pointer
    def insert(self,node):
        previous,nxt = self.right.prev,self.right
        previous.next = nxt.prev = node
        node.next,node.prev = nxt, previous #self.right, self.right.prev
        
    #remove node from list  
    def remove(self,node):
        previous,nxt  = node.prev,node.next
        nxt.prev,previous.next = previous,nxt
        
        

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            #need to update the recency in the linked list aka helper functions
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
            
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        #insert node into the dictionary
        self.cache[key] = Node(key,value)
        #insert node into the linkedlist
        self.insert(self.cache[key])
        
        if len(self.cache)> self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key ]
          

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#fast lookups = hash table, fast lookups
#doubly linked list = can remove in constant time and won have to resize,fast removals
#Question
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
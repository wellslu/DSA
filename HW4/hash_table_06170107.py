from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.capacity=capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        h = MD5.new()
        h.update(key.encode('utf-8'))
        node = self.data[int(h.hexdigest(),16)%self.capacity]
        if node == None:
            self.data[int(h.hexdigest(),16)%self.capacity] = ListNode(key)
        else:
            while node.next != None:
                node = node.next
            node.next = ListNode(key)
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        h = MD5.new()
        h.update(key.encode('utf-8'))
        node = self.data[int(h.hexdigest(),16)%self.capacity]
        if node == None:
            return
        else:
            if node.val == key:
                self.data[int(h.hexdigest(),16)%self.capacity] = node.next
            else:
                while node.next != None:
                    if node.next.val == key:
                        node.next = node.next.next
                    node = node.next
                    if node == None:
                        break
            
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        h = MD5.new()
        h.update(key.encode('utf-8'))
        node = self.data[int(h.hexdigest(),16)%self.capacity]
        while node != None:
            if node.val == key:
                return True
            else:
                node = node.next
        return False

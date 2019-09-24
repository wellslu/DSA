class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next=None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.val == None:
            return -1
        j=self
        i=0
        while j!=None:
            if i == index:
                return j.val
            j=j.next
            i+=1
        return -1

        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val==None:
            self.val=val
        elif self!=None:
            self.val=val
            
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val==None:
            self.val=val
        elif self.val!=None:
            j=self
            i=0
            while j.next!=None:
                j=j.next
                i+=1
            j.next=MyLinkedList()
            j.next.val=val
        
        
        

    def addAtIndex(self, index: int, val: int) -> None:#在第幾項插入值
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index<=0:
            j=self
            n=self.next
            self.val=val
            self.next=MyLinkedList()
            self.next=n
            
        i=1
        j=self
        n=j.next
        while i<index:
            if j != None:
                j=j.next
                i+=1
                n=j
            else:
                return
        j.next=MyLinkedList()
        j.next.val=val
        j.next.next=n
            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i=0
        j=self
        n=j.next
        while i < index:
            i+=1
            j=j.next
            n=n.next
        j.next=MyLinkedList()
        j.val=n.val
        j.next=n.next
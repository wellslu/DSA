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
        else:
            j=self.val
            n=self.next
            self.val=val
            self.next=MyLinkedList()
            self.next.val=j
            self.next.next=n
            
        
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
        i=0
        t=0
        j=self
        n=j
        index=index-1
        while i<index:
            i+=1
            if j.next!=None:
                j=j.next
                n=j
            else:
                t+=1
        if index<=-1:
            self.addAtHead(val)
        elif t==0 and j.next!=None:
            n=j.next
            j.next=MyLinkedList()
            j.next.val=val
            j.next.next=n
        elif t<=1 and j.val!=None:
            self.addAtTail(val)
            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i=0
        j=self
        n=j
        t=0
        while i<index:
            i+=1
            if j.next!=None:
                n=j
                j=j.next
            else:
                t+=1
        if index==0 and j.next==None:
            j.val=None
        elif index>=0 and t==0 and j.next!=None:
            j.val=j.next.val
            j.next=j.next.next
        elif index>0 and t==0 and j.val!=None:
            n.next=None
        else:
            return
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

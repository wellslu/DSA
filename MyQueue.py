class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x=None
        self.next=None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.x==None:
            self.x=x
        elif self.x!=None:
            j=self
            while j.next!=None:
                j=j.next
            j.next=MyQueue()
            j.next.x=x

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        j=self
        i=self.x
        if j.x != None and j.next == None:
            j.x = None
        elif j.next != None:
            j.x = j.next.x
            j.next = j.next.next
        return i

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.x

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.x == None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
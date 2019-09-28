class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.x=None
        self.next=None
        self.min=None

    def push(self, x: int) -> None:
        j=self
        if j.x == None:
            j.x = x
            j.min = x
        elif j.x != None:
            while j.next!=None:
                j=j.next
            j.next=MinStack()
            j.next.x=x
            if x < self.min:
                self.min = x

    def pop(self) -> None:
        j=self
        if j.next == None and j.x != None:
            j.x = None
            j.mix = None
        elif j.next != None:
            while j.next != None:
                n=j
                j=j.next
            if j.x == self.min:
                n.next = None
                a = self
                b = self.x
                while a.next != None:
                    a = a.next
                    if a.x < b:
                        b=a.x
                self.min = b
            else:
                n.next = None

    def top(self) -> int:
        j = self
        if j.next == None and j.x != None:
            return j.x
        elif j.next != None:
            while j.next != None:
                j=j.next
            return j.x

    def getMin(self) -> int:
        if self.min != None:
            return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

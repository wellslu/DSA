class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.x=None
        self.next=None

    def push(self, x: int) -> None:
        j=self
        #若linkedlist中沒有任何數字則直接當第一個
        if j.x == None:
            j.x = x
        #若有數字則數到最後一個時並在尾端加上去
        elif j.x != None:
            while j.next!=None:
                j=j.next
            j.next=MinStack()
            j.next.x=x

    def pop(self) -> None:
        j=self
        #若只有一個數字時，則直接把唯一數字變成None
        if j.next == None and j.x != None:
            j.x == None
        #若有linkedlist時，則數到最後面，把指向最後一個數字刪掉
        elif j.next != None:
            while j.next != None:
                n=j
                j=j.next
            n.next = None

    def top(self) -> int:
        j = self
        #若只有一個數字，則直接回傳
        if j.next == None and j.x != None:
            return j.x
        #若有linkedlist時，則數到最後一個數回傳
        elif j.next != None:
            while j.next != None:
                j=j.next
            return j.x

    def getMin(self) -> int:
        j = self
        i = self.x
        #若只有一個數字，則直接回傳
        if j.next == None and j.x != None:
            return j.x
        #若有linkedlist時，則一一比對，當出現比較小的數字時，最小值i則替換成較小的數字
        elif j.next != None:
            while j.next != None:
                j = j.next
                if j.x != None and j.x < i:
                    i=j.x
            return i

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

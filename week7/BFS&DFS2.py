from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        queue = []
        ans = []
        ans.append(s)
        queue = queue+self.graph[s]
        while len(queue) != 0:
            s = queue.pop(0)
            ans.append(s)
            add = []
            add = add+self.graph[s]
            for i in add:
                if i in queue:
                    add.remove(i)
            queue = queue + add
            for i in ans:
                if i in queue:
                    queue.remove(i)
        return ans
    def DFS(self, s):
        stack = []
        ans = []
        ans.append(s)
        stack = stack+self.graph[s]
        while len(stack) != 0:
            s = stack.pop()
            ans.append(s)
            add = []
            add = add+self.graph[s]
            for i in add:
                if i in stack:
                    add.remove(i)
            stack = stack + add
            for i in ans:
                if i in stack:
                    stack.remove(i)
        return and

if __name__ == "__main__":
	g=Graph()
	g.addEdge(0,1)
	g.addEdge(0,2)
	g.addEdge(1,2)
	g.addEdge(2,0)
	g.addEdge(2,3)
	g.addEdge(3,3)
	print(g.graph) # defaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})
	print(g.DFS(2)) # [2, 3, 0, 1]
	print(g.graph) # defaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})
	print(g.BFS(2)) # [2, 0, 3, 1]

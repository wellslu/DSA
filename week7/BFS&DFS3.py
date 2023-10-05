from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s): 
        queue = []
        final = []
        final.append(s)
        queue = queue+self.graph[s]
        while len(queue) != 0:
            s = queue.pop(0)
            final.append(s)
            plus = []
            plus = plus+self.graph[s]
            for i in plus:
                if i in queue:
                    plus.remove(i)
            for i in plus:
                if i in final:
                    plus.remove(i)
            queue = queue+plus
        return final
    def DFS(self, s):
        stack = []
        final = []
        final.append(s)
        stack = stack+self.graph[s]
        while len(stack) != 0:
            s = stack.pop()
            final.append(s)
            plus = []
            plus = plus+self.graph[s]
            for i in plus:
                if i in stack:
                    plus.remove(i)
            for i in plus:
                if i in final:
                    plus.remove(i)
            stack = stack+plus
        return final

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

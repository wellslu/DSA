from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        queue = []
        final = []
        final.append(s)
        queue = queue+self.graph[s]
        while len(queue) != len(final)-1:
            for i in queue:
                if i in final:
                    continue
                final.append(i)
                for n in self.graph[i]:
                    if n not in queue:
                        if n not in final:
                            queue.append(n)
                break
        return final
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        stack = []
        final = []
        final.append(s)
        stack = stack+self.graph[s]
        while len(stack) != len(final)-1:
            for i in reversed(stack):
                if i in final:
                    continue
                final.append(i)
                for n in self.graph[i]:
                    if n not in stack:
                        if n not in final:
                            stack.append(n)
                break
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

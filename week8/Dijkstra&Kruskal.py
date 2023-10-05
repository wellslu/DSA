from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.dict = defaultdict(list) 
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
        self.dict[w].append([u,v])
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
        answer = {}
        for num in range(self.V):
            final = self.graph[num]
            for i in range(self.V):
                for each in range(len(final)):
                    if final[each] != 0:
                        nextlist = self.graph[each]
                        for deep in range(len(nextlist)):
                            if nextlist[deep] != 0:
                                if final[deep] == 0 or final[deep] > final[each] + nextlist[deep]:
                                    final[deep] = final[each] + nextlist[deep]
            self.graph[num] = final
        
        for i in range(self.V):
            self.graph[i][i] = 0
            
        for i in range(self.V):
            answer[str(i)] = self.graph[s][i]
            
        return answer
    def Kruskal(self):
        """
        :rtype: dict
        """
        answer={}
        check = [column for column in range(self.V)]  
        val = sorted(self.dict)
        for i in val:
            for f,s in self.dict[i]:
                if check[f] == check[s]:
                    pass
                else:
                    check = [check[f] if x==check[s] else x for x in check]
                    answer[str(f)+'-'+str(s)] = i
        return answer

if __name__ == "__main__":
	g = Graph(9)
	g.graph = [[0,4,0,0,0,0,0,8,0],
	          [4,0,8,0,0,0,0,11,0],
	          [0,8,0,7,0,4,0,0,2],
	          [0,0,7,0,9,14,0,0,0],
	          [0,0,0,9,0,10,0,0,0],
	          [0,0,4,14,10,0,2,0,0],
	          [0,0,0,0,0,2,0,1,6],
	          [8,11,0,0,0,0,1,0,7],
	          [0,0,2,0,0,0,6,7,0]]
	
	print('Dijkstra',g.Dijkstra(0)) # Dijkstra {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}
	
	g = Graph(4)
	g.addEdge(0,1,10)
	g.addEdge(0,2,6)
	g.addEdge(0,3,5)
	g.addEdge(1,3,15)
	g.addEdge(2,3,4)
	print('Kruskal',g.Kruskal()) # Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}

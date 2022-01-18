import collections
from pprint import pprint

"""
Can they escape?
"""
def escape_temple(N, corridor, trap, adventurer, out):
    res_G = [[0] * (2*N + 2) for _ in range(2*N + 2)]
    for u, v in corridor:
    	res_G[u+N][v] = float("inf")
    	res_G[u][v+N] = float("inf")
    	if res_G[u][u+N] == 0 and trap[u]: # pas encore initialisé
    		#is_adv = trap[u] in adventurer # si y'a un aventurier dessus
    		res_G[u][u+N] = trap[u]
    		#res_G[u+N][u] = trap[u]
    	if res_G[v][v+N] == 0 and trap[v]:
    		#is_adv = trap[v] in adventurer
    		res_G[v][v+N] = trap[v]
    for s in adventurer:
    	res_G[2*N][s] = float("inf")
    for t in out:
    	res_G[t+N][2*N + 1] = float("inf")
    res_G[9][3]=0
    res_G[3][13] = 0
    pprint(res_G)
    g = Graph(res_G)
    return (g.FordFulkerson(2*N, 2*N+1) - len(adventurer) ) >= 0

def bfs(N, res_G, source, target):
    parent = [0] * N
    visited = [0] * N

    queue = []
    queue.insert(0, source)
    visited[source] = True
    parent[source] = -1
    while len(queue) != 0:
        u = queue.pop()
        for v in range(N):
            if not visited[v] and res_G[u][v] > 0:
                queue.insert(0, v)
                parent[v] = u
                visited[v] = True

    return visited[target] == True, parent 

class Graph:
    def __init__(self,graph):
        self.graph = graph # residual graph
        self. ROW = len(graph)
        #self.COL = len(gr[0])   
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent):
        # Mark all the vertices as not visited
        visited =[False]*(self.ROW)     
        # Create a queue for BFS
        queue=[]      
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        # Standard BFS Loop
        while queue: 
            #Dequeue a vertex from queue and print it
            u = queue.pop(0)
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False    
    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
        max_flow = 0 # There is no flow initially
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            # Add path flow to overall flow
            max_flow +=  path_flow
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow
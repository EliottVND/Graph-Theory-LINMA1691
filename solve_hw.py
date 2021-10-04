import sys
from collections import defaultdict, deque



# """
# Prends comme inputs:
# 		-adj: liste d'adjacence du graphe dirigé décrivant la dynamique de dispersion des rumeurs
# 	output:
# 		-nombre solution du problème pour la dynamique donnée par adj
# """
# def dfs_visit(G, s, parent, stack):
#     """ Recursively explore all childrens of s """
#     global time
#     time += 1
#     s.d = time

#     for v in G.adj[s]:
#         if v not in parent:
#             parent[v] = s
#             dfs_visit(G, v, parent, stack)

#     time += 1
#     s.f = time
#     stack.append(s)


# def dfs(G, stack):
#     """ Explore the whole graph using Depth First Search """
#     parent = {}
#     stack = []

#     for vertex in list(G.adj.keys()):
#         if vertex not in parent:
#             parent[vertex] = None
#             dfs_visit(G, vertex, parent, stack)

#     return stack
# # ==============================================================================

# # ==============================================================================
# # Helper DFS function and Kosaraju's Algorithm

# def dfs_single_visit(adj_list, v, visited, stack):
#     """ Recursively visits all the children of v """
#     for u in adj_list[v]:
#         if u not in visited:
#             visited[u] = v
#             dfs_single_visit(adj_list, u, visited, stack)
#     stack.append(v)

# def kosaraju(G):
#     """ Kosaraju's Algorithm for finding strongly connected components. """
#     # get vertices based on their finishing time in decreasing order
#     stack = dfs(G, [])
    
#     # Reverse edges of the graph G
#     rev_adj = {}

#     for vertex in G.adj.keys():
#         rev_adj[vertex] = {}

#     for vertex in G.adj.keys():
#         for u in G.adj[vertex]:
#             rev_adj[u][vertex] = True


#     # Traverse graph by popping vertices out from the stack
#     visited = {}
#     components = []
#     i = 0

#     while stack != []:
#         v = stack.pop()
#         # if v is already visited skip iteration
#         if v in visited:
#             continue
#         # otherwise find all the vertices it can reach and put them into components
#         else:
#             components.append([])
#             if v not in visited:
#                 visited[v] = True
#                 dfs_single_visit(rev_adj, v, visited, components[i])
            
#             components.append([])
#             i += 1
#     return components


def solve(adj):
    # findSCC(adj)
    # print(f"{adj=}")
    G = adj
    # postorder DFS on G to transpose the graph and push root vertices to stack
    N = len(G)
    T = [[] for _ in range(N)]
    stack = []
    visited = [False] * N
    for u in range(N):
        if not visited[u]: # visited?
            visited[u], S = True, [u] # alors visité et Stack = [u]
            while S: # tant que Stack remplie
                u, done = S[-1], True # Peek et potentiellement aucune sortie après u
                for v in G[u]: # on regarde sur chaque élément de la liste d'adjacence de u
                    T[v].append(u) # on fait le reverse en même temps
                    if not visited[v]: # si v n'est pas visité
                        visited[v], done = True, False # on le visite et done = False
                        S.append(v) # on le push sur la stack
                        break # on ajoute que le premier élément
                if done: # plus rien à faire avec le noeud u (soit tous visités soit plus d'arêtes)
                    S.pop() # fini
                    stack.append(u) # le truc qu'on return

    # postorder DFS on T to pop root vertices from stack and mark SCCs
    
    # print(f"{T=}") # reversed
    # print(f"{stack=}") # stack utilisé
    
    SCC = [None] * N
    curr_SCC_index = -1
    while stack: # tant qu'on a un stack non vide
        curr_SCC_index+=1
        root = stack.pop() # on récupère l'élément au top
        internal_stack = [root] # on crée un stack interne

        if visited[root]: # si visité
            visited[root] = False
            SCC[root] = root
        
        while S: # S interne donc au début = [r]
            u, done = internal_stack[-1], True # on prend le top et done = True
            for v in T[u]: # liste d'adjacence du transposé
                if visited[v]: # si pas visité dans le reverse
                    visited[v] = done = False # done à false pour éviter de pop
                    internal_stack.append(v) # on le push sur la stack
                    SCC[v] = curr_SCC_index # on dit que v appartient au SCC n°i
                    # dict[root] = C[current_index].append(G[v])
                    break
            if done:
                internal_stack.pop()
    print(f"{SCC=}")
    adj_SCC=[[] for _ in range(SCC[-1]+1)] # équivalent à C[-1]+1
    for i, curr_node_adj in enumerate(G): # on boucle sur les noeuds du graphe
        for out_node in curr_node_adj:
            if (SCC[i] != SCC[out_node]) and (SCC[out_node] not in adj_SCC[SCC[i]]):
                adj_SCC[SCC[i]].append(SCC[out_node])
    is_source = [True] * N
    for curr_node_adj in adj_SCC:
        for out_node in curr_node_adj:
            is_source[out_node] = False
    print(f"{adj_SCC=}")
    print(f"{curr_SCC_index=}")
    return sum(is_source)

# def DFS(adj_list):
#     visited = [False for i in range(len(adj_list))]

#     # Create a stack for DFS
#     stack = []

#     # Push the current source node.
#     stack.append(0)

#     while (len(stack)):
#         # Pop a vertex from stack and prin it
#         s = stack.pop()

#         # Stack may contain same vertex twice. So
#         # we need to prin the popped item only
#         # if it is not visited.
#         if (not visited[s]):
#             print(s,end=' ')
#             visited[s] = True

#         # Get all adjacent vertices of the popped vertex s
#         # If a adjacent has not been visited, then push it
#         # to the stack.
#         for node in adj_list[s]:
#             if (not visited[node]):
#                 stack.append(node)
    

# def reverse_graph(adj):
#     rev = [[] for _ in range(len(adj))]
#     for i in range(len(adj)):
#         for j in adj[i]:
#             rev[j].append(i)
#     return rev


# def DFSIterativeDaniel(adj, start_index, visited, stack_to_return):
#     print(adj)
#     stack = deque()
#     stack.append(start_index)
#     while stack :
#         src = stack.popleft()
#         if not visited[src] :
#             visited[src] = True
#             print(src, end = ' ')
#             stack_to_return.append(src)
#             if adj[src] != []:
#                 for adj_node in adj[src] :
#                     if not visited[adj_node]:
#                         stack.appendleft(adj_node)
#     return stack_to_return


# def DFSIterativeCours(adj, start_index, visited, stack_to_return):
#     print(adj)
#     stack = deque()
#     stack.append(start_index)
#     while stack :
#         src = stack.peek()
#         if not visited[src] :
#             visited[src] = True
#             #print(src, end = ' ')
#             #stack_to_return.append(src)
#             if adj[src] != []:
#                 for adj_node in adj[src] :
#                     if not visited[adj_node]:
#                         stack.append(adj_node)
#     return stack_to_return


# def DFSIterative2(adj, start_index, visited):
#     stack = deque()
#     stack.append(start_index)
#     while stack :
#         src = stack.popleft()
#         if not visited[src] :
#             visited[src] = True
#             print(src, end = ' ')
#             if adj[src] != []:
#                 for adj_node in adj[src] :
#                     stack.appendleft(adj_node)

# def findSCC(adj):
#     n_V = len(adj)
#     visited = [False] * n_V
#     stack = deque()
#     for i in range(n_V):
#         if(not visited[i]):
#             DFSIterative(adj, i, visited, stack)
#     print(f"{stack=}")
#     visited = [False] * n_V
#     reversed = reverse_graph(adj)
#     while stack:
#         top = stack.pop()
#         if(not visited[top]):
#             DFSIterative2(reversed, top, visited)
#             print()


"""
    codes pour les tests
"""

def read_and_solve_tests(input_file, output_file):
    f_in = open(input_file, "r")
    f_out = open(output_file, "w")

    nProb = int(f_in.readline())
    for p in range(nProb):
        adj = load_graph(f_in)

        f_out.write(str(solve(adj))+"\n")

    f_in.close()
    f_out.close()


def load_num(f_in):
    num_str = f_in.readline()

    return list(map(int, num_str.split()))


"""stackoad graph into its adjacency list"""
def load_graph(f_in):
    N,E = load_num(f_in)

    # stackoad each edge an construct adjacency list
    adj = [list() for v in range(N)]

    for i in range(E):
        x,y = load_num(f_in)
        adj[x-1].append(y-1)

    return adj


if __name__ == '__main__':

    nProb = int(sys.stdin.readline())
    for p in range(nProb):
        adj = load_graph()

        solve(adj)

    exit(0)

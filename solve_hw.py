import sys
from collections import defaultdict, deque



"""
Prends comme inputs:
		-adj: liste d'adjacence du graphe dirigé décrivant la dynamique de dispersion des rumeurs
	output:
		-nombre solution du problème pour la dynamique donnée par adj
"""
def dfs_visit(G, s, parent, stack):
    """ Recursively explore all childrens of s """
    global time
    time += 1
    s.d = time

    for v in G.adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(G, v, parent, stack)

    time += 1
    s.f = time
    stack.append(s)


def dfs(G, stack):
    """ Explore the whole graph using Depth First Search """
    parent = {}
    stack = []

    for vertex in list(G.adj.keys()):
        if vertex not in parent:
            parent[vertex] = None
            dfs_visit(G, vertex, parent, stack)

    return stack
# ==============================================================================

# ==============================================================================
# Helper DFS function and Kosaraju's Algorithm

def dfs_single_visit(adj_list, v, visited, stack):
    """ Recursively visits all the children of v """
    for u in adj_list[v]:
        if u not in visited:
            visited[u] = v
            dfs_single_visit(adj_list, u, visited, stack)
    stack.append(v)

def kosaraju(G):
    """ Kosaraju's Algorithm for finding strongly connected components. """
    # get vertices based on their finishing time in decreasing order
    stack = dfs(G, [])
    
    # Reverse edges of the graph G
    rev_adj = {}

    for vertex in G.adj.keys():
        rev_adj[vertex] = {}

    for vertex in G.adj.keys():
        for u in G.adj[vertex]:
            rev_adj[u][vertex] = True


    # Traverse graph by popping vertices out from the stack
    visited = {}
    components = []
    i = 0

    while stack != []:
        v = stack.pop()
        # if v is already visited skip iteration
        if v in visited:
            continue
        # otherwise find all the vertices it can reach and put them into components
        else:
            components.append([])
            if v not in visited:
                visited[v] = True
                dfs_single_visit(rev_adj, v, visited, components[i])
            
            components.append([])
            i += 1
    
    return components
def solve(adj):
    findSCC(adj)
    G = adj
    # postorder DFS on G to transpose the graph and push root vertices to L
    N = len(G)
    T, L, U = [[] for _ in range(N)], [], [False] * N
    for u in range(N):
        if not U[u]:
            U[u], S = True, [u]
            while S:
                u, done = S[-1], True
                for v in G[u]:
                    T[v].append(u)
                    if not U[v]:
                        U[v], done = True, False
                        S.append(v)
                        break
                if done:
                    S.pop()
                    L.append(u)
    # postorder DFS on T to pop root vertices from L and mark SCCs
    print(f"{T=}")
    print(f"{L=}")
    
    C = [None] * N
    while L:
        r = L.pop()
        S = [r]
        if U[r]:
            U[r], C[r] = False, r
        while S:
            u, done = S[-1], True
            for v in T[u]:
                if U[v]:
                    U[v] = done = False
                    S.append(v)
                    C[v] = r
                    break
            if done:
                S.pop()

    return len(set(C))

def DFS(adj_list):
    visited = [False for i in range(len(adj_list))]

    # Create a stack for DFS
    stack = []

    # Push the current source node.
    stack.append(0)

    while (len(stack)):
        # Pop a vertex from stack and print it
        s = stack.pop()

        # Stack may contain same vertex twice. So
        # we need to print the popped item only
        # if it is not visited.
        if (not visited[s]):
            print(s,end=' ')
            visited[s] = True

        # Get all adjacent vertices of the popped vertex s
        # If a adjacent has not been visited, then push it
        # to the stack.
        for node in adj_list[s]:
            if (not visited[node]):
                stack.append(node)
    

def reverse_graph(adj):
    rev = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in adj[i]:
            rev[j].append(i)
    return rev

def DFSIterative(adj, start_index, visited, stack_to_return):
    print(adj)
    stack = deque()
    stack.append(start_index)
    while stack :
        src = stack.popleft()
        if not visited[src] :
            visited[src] = True
            print(src, end = ' ')
            stack_to_return.append(src)
            if adj[src] != []:
                for adj_node in adj[src] :
                    stack.appendleft(adj_node)
    return stack_to_return


def DFSIterative2(adj, start_index, visited):
    stack = deque()
    stack.append(start_index)
    while stack :
        src = stack.popleft()
        if not visited[src] :
            visited[src] = True
            print(src, end = ' ')
            if adj[src] != []:
                for adj_node in adj[src] :
                    stack.appendleft(adj_node)

def findSCC(adj):
    n_V = len(adj)
    visited = [False] * n_V
    stack = deque()
    for i in range(n_V):
        if(not visited[i]):
            DFSIterative(adj, i, visited, stack)
    print(f"{stack=}")
    visited = [False] * n_V
    reversed = reverse_graph(adj)
    while stack:
        top = stack.pop()
        if(not visited[top]):
            DFSIterative2(reversed, top, visited)
            print()


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


"""Load graph into its adjacency list"""
def load_graph(f_in):
    N,E = load_num(f_in)

    # Load each edge an construct adjacency list
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

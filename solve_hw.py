import sys
from collections import defaultdict, deque


def solve(adj, diff=False):
    solve.count += 1
    # findSCC(adj)
    # print(f"{adj=}")
    
    # postorder DFS on G to transpose the graph and push root vertices to stack
    N = len(adj)
    G = adj # [list(set(el)) for el in adj]
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
    C = [None] * N
    curr_SCC_index = -1
    prev_root = None
    while stack: # tant qu'on a un stack non vide
        
        root = stack.pop() # on récupère l'élément au top
        if root != prev_root:
            curr_SCC_index+=1
            prev_root = root    
        S = [root] # on crée un stack interne

        if visited[root]: # si visité
            visited[root] = False
            SCC[root] = curr_SCC_index
            C[root] = root
        while S: # S interne donc au début = [r]
            u, done = S[-1], True # on prend le top et done = True
            for v in T[u]: # liste d'adjacence du transposé
                if visited[v]: # si pas visité dans le reverse
                    visited[v] = done = False # done à false pour éviter de pop
                    S.append(v) # on le push sur la stack
                    SCC[v] = curr_SCC_index # on dit que v appartient au SCC n°i
                    # dict[root] = C[current_index].append(G[v])
                    C[v] = root
                    break
            if done:
                S.pop()
    if diff:
        print(SCC)
        print(C) 
    index = -1
    unique_roots = list(set(C))
    d= {}
    for i in range(len(unique_roots)):
        d[unique_roots[i]] = i
    for j in range(len(SCC)):
        SCC[j] = d[C[j]]
    if diff:
        print(SCC)
        print(C) 
    adj_SCC=[[] for _ in range(curr_SCC_index + 1)] # équivalent à C[-1]+1
    for i, curr_node_adj in enumerate(G): # on boucle sur les noeuds du graphe
        for out_node in curr_node_adj:
            # print(SCC[i])
            # print(len(adj_SCC))
            if (SCC[i] != SCC[out_node]) and (SCC[out_node] not in adj_SCC[SCC[i]]):
                adj_SCC[SCC[i]].append(SCC[out_node])
    is_source = [True] * N
    for curr_node_adj in adj_SCC:
        for out_node in curr_node_adj:
            is_source[out_node] = False
    nb_sources = sum(is_source)
    if solve.count == 5:
        print(f"{solve.count=}")
        print(f"{adj=}")
        print(f"{G=}")
        print(f"{SCC=}")
        print(f"{C=}")
        print(f"{adj_SCC=}")
        print(f"{(curr_SCC_index+1)=}")
        print()
    return nb_sources if nb_sources != 0 else 1


"""
    codes pour les tests
"""

def read_and_solve_tests(input_file, output_file):
    f_in = open(input_file, "r")
    f_out = open(output_file, "w")
    solve.count = 0
    nProb = int(f_in.readline())
    for p in range(nProb):
        adj = load_graph(f_in)

        f_out.write(str(solve(adj))+"\n")
    G = [[1], [0, 2], [0, 3, 4], [4], [5], [6], [4], [6]]

    print(solve(G, True))
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

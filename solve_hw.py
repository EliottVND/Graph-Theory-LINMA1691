import sys


def solve(adj):
    
    # postorder DFS on G to transpose the graph and push root vertices to stack
    N = len(adj)
    G = adj 
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
    
    SCC = [None] * N
    #C = [None] * N
    curr_SCC_index = 0
    while stack: # tant qu'on a un stack non vide
        root = stack.pop() # on récupère l'élément au top 
        S = [root] # on crée un stack interne

        if visited[root]: # si pas visité avec le 2e passage
            visited[root] = False # alors visité par le 2e passage
            SCC[root] = curr_SCC_index # le SCC du root = current_Scc_index
            #C[root] = root
            while S: # S interne donc au début = [r]
                u = S[-1] # on prend le top
                done = True  # et done = True
                for v in T[u]: # liste d'adjacence du transposé
                    if visited[v]: # si pas visité dans le reverse
                        visited[v] = False # mtnt il est visité
                        done = False # done à false pour éviter de pop
                        S.append(v) # on le push sur la stack
                        SCC[v] = curr_SCC_index # on dit que v appartient au SCC n°i
                        # C[v] = root
                        break
                if done:
                    S.pop()
            curr_SCC_index+=1

    adj_SCC=[[] for _ in range(curr_SCC_index)]
    for i, curr_node_adj in enumerate(G): # on boucle sur les noeuds du graphe
        for out_node in curr_node_adj: # on regarde dans sa liste d'adjacence
            if (SCC[i] != SCC[out_node]) and (SCC[out_node] not in adj_SCC[SCC[i]]):
                adj_SCC[SCC[i]].append(SCC[out_node])
                
    is_source = [True] * curr_SCC_index
    for curr_node_adj in adj_SCC:
        for out_node in curr_node_adj:
            is_source[out_node] = False
    nb_sources = sum(is_source)

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

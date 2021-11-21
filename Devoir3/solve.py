# from queue import Queue

"""
    in:
        -N le nombre de noeuds
        -adj liste d'adjacence avec les indices commençant à zéro
    out:
        -True or False, si le graphe est décomposable en une union de K_1,6 disjoint sur les arêtes ou non
"""
def decomposition(N, adj):

    color = [-1] * N

    # Assign first color to source vertex
    color[0] = 1

    # Create a queue of vertex to run BFS from src vertex.
    queue = [0]

    # Run while vertices are in the queue
    while len(queue) != 0:
        # Taking the first node from the queue
        node = queue[0]
        queue.pop(0)

        # Traversing adjacency list of the current node
        for neighbour in adj[node]:
            # Check if the neighbour is assigned any color or not.
            if color[neighbour] == -1:
                # If the color of current node is 1 assign color 0 to neighbour otherwise assign color 1.
                color[neighbour] = color[node] ^ 1
                queue.append(neighbour)

            # If the color of current node and neighbouring node is same the the graph is not bipartite.
            if color[neighbour] == color[node]:
                return False
    return True

def load_num(f_in):
    num_str = f_in.readline()

    return list(map(int, num_str.split()))


def load_graph(f_in):
    """Load graph into its adjacency list"""
    N,E = load_num(f_in)

    # Load each edge an construct adjcency  list
    adj = [list() for v in range(N)]

    for i in range(E):
        x,y = load_num(f_in)
        adj[x].append(y)
        adj[y].append(x)

    return adj

def check_code(input_file, output_file):
    f_in = open(input_file, "r")
    f_out = open(output_file, "r")

    nProb = int(f_in.readline())
    ok = True
    for p in range(nProb):
        adj = load_graph(f_in)

        ans = int(decomposition(len(adj),adj))
        
        l = f_out.readline()

        if ans!=int(l.split()[0]):
            ok = False
            break

    f_in.close()
    f_out.close()

    return ok

if __name__ == "__main__":
    input_file = "tests/input.txt"
    expected_output_file = "tests/output.txt"

    ok = check_code(input_file,expected_output_file)
    if not ok:
        print("Difference between the answer and the expected output")
    else:
        print("Tests are ok :)")

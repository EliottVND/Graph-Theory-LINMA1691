import sys
from collections import deque



"""
Prends comme inputs:
		-adj: liste d'adjacence du graphe dirigé décrivant la dynamique de dispersion des rumeurs
	output:
		-nombre solution du problème pour la dynamique donnée par adj
"""
def solve(adj):
	""" TODO """
    """ vous êtes libre de créer des function annexes, etc... et aussi d'importer d'autres package standards"""
	
    return """ solution """



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

    # Load each edge an construct adjcency  list
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

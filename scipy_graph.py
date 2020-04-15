import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import shortest_path

def get_path(Pr, i, j):
    path = [j]
    k = j
    while Pr[i, k] != -9999:
        path.append(Pr[i, k])
        k = Pr[i, k]
    return path[::-1]

G_dense = [ [0,     0,  0,  13, 0,  0,  2,  0,  0,  0,  0],
            [1,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [25,    2,  0,  0,  30, 0,  0,  0,  0,  0,  0],
            [0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [0,     5,  0,  0,  0,  4,  0,  14, 0,  0,  0],
            [0,     0,  11, 0,  0,  0,  0,  0,  9,  0,  0],
            [0,     0,  0,  12, 0,  17, 0,  0,  8,  0,  0],
    [0,0,0,0,0,0,0,0,3,0,6],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,8,0,0],
    [0,0,0,0,0,0,0,0,0,7,0]]

INICIO = 0
FIM = 1
print("START: " + str(INICIO))
print("END: " + str(FIM))
print("")

print("##### scipy floyd_warshall")
graph = csr_matrix(G_dense)
dist_matrix, predecessors = floyd_warshall(csgraph=graph, directed=False, return_predecessors=True)
print("##### Route:")
print(get_path(predecessors, 0,4))
print("##### Distance:")
print(dist_matrix[0][4])

print("")
print("##### scipy shortest_path")
D, Pr = shortest_path(G_dense, directed=False, method='FW', return_predecessors=True)
print("##### Route:")
print(get_path(Pr, 0,4))
print("##### Distance:")
print(D[0][4])

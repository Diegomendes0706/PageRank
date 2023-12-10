import numpy as np
import networkx as nx
import scipy


def pagerank(grafo, d, M, i):
    n = len(grafo)
    E = np.ones((n, n), dtype=int)
    A = (1 - d) / n * E + d * M
    P = np.ones((n, 1)) / n
    for c in range(i):
        pr = A @ P
        P = pr
    return pr


grafo = {'1': ["4"], '2': ['1', '3'], '3': ['4'], '4': ['2']}
G = nx.DiGraph(grafo)

m = nx.linalg.graphmatrix.adjacency_matrix(G).todense()  # pega a matriz que marca com 1 as conexoes
m = m.astype(float)  # transforma em tipo flutuante
for c in m:
    c /= sum(c)  # divide pelo total de conexões
M = np.array(m).T  # faz a matriz transposta

interacoes = int(input("quantas interções? "))
for i in grafo:
    print(f"{i} - pagerank: {pagerank(grafo, 0.85, M, interacoes)[int(i)-1][0]} ")

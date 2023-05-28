
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal_mst(edges, num_vertices):
    result = []
    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    parent = list(range(num_vertices))
    rank = [0] * num_vertices

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            result.append((u, v, w))
            union(parent, rank, u, v)

    return result
edges = [(0, 1, 4), (0, 7, 8), (1, 7, 11), (1, 2, 8), (2, 3, 7)]

num_vertices = 9

mst = kruskal_mst(edges, num_vertices)
print(mst)
'''
o/p-
G:\Ai programs>python kruskal_algo.py
[(0, 1, 4), (2, 3, 7), (0, 7, 8), (1, 2, 8)]
'''


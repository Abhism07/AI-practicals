def sort_arr():
    Arr=[]
    n = int(input("Enter the number of elements:"))
    for i in range (n):
        ele = int(input("enter elements:"))
        Arr.append(ele)
    
    for i in range (len(Arr)):
        ind=i
        for j in range (i+1,len(Arr)):
            if (Arr[ind]>Arr[j]):
                ind=j
        Arr[i],Arr[ind] = Arr[ind],Arr[i]
    print("Sorted Array:")
    for i in range (len(Arr)):
        print(Arr[i],end=" ")
	

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

# Get user input for the edges
edges = []
num_vertices = int(input("Enter the number of vertices: "))

for i in range (num_vertices):
    u, v, w = map(int,input("Enter u v w :").split())
    edges.append((u, v, w))


# Find and print the minimum spanning tree
mst = kruskal_mst(edges, num_vertices)
print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} -- {v} : {w}")

sort_arr()


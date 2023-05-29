def solve_graph_coloring(graph):
    num_vertices = len(graph)
    colors = [-1] * num_vertices
    solution = []

    def solve(vertex):
        if vertex == num_vertices:
            return True

        sorted_colors = sort_colors_by_frequency(vertex)

        for color in sorted_colors:
            if is_safe(vertex, color):
                colors[vertex] = color
                if solve(vertex + 1):
                    return True
                colors[vertex] = -1

        return False

    def is_safe(vertex, color):
        for adjacent_vertex in graph[vertex]:
            if colors[adjacent_vertex] == color:
                return False
        return True

    def sort_colors_by_frequency(vertex):
        frequency = [0] * num_vertices

        for i in range(vertex):
            if colors[i] != -1:
                frequency[colors[i]] += 1
    #Sorting in descending order
        sorted_colors = sorted(range(num_vertices), key=lambda x: frequency[x], reverse=True)
        return sorted_colors

    def print_solution():
        color_map = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
        for vertex in range(num_vertices):
            solution.append((vertex, color_map[colors[vertex]]))
        print("Vertex Colors:", solution)

    if solve(0):
        print_solution()
    else:
        print("No solution exists.")


num_vertices = int(input("Enter the number of vertices: "))
graph = [[] for _ in range(num_vertices)]
for vertex in range(num_vertices):
    neighbors = input(f"Enter the neighbors of vertex {vertex} (space-separated): ").split()
    graph[vertex] = [int(neighbor) for neighbor in neighbors]

solve_graph_coloring(graph)
'''
o/p - 
G:\Ai programs>python color_map.py
Enter the number of vertices: 4
Enter the neighbors of vertex 0 (space-separated): 1 2 3
Enter the neighbors of vertex 1 (space-separated): 0 2
Enter the neighbors of vertex 2 (space-separated): 1 0
Enter the neighbors of vertex 3 (space-separated): 0 2
Vertex Colors: [(0, 'Red'), (1, 'Green'), (2, 'Blue'), (3, 'Green')]
'''

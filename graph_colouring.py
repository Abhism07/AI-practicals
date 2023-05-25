def solve_graph_coloring(graph):
    num_vertices = len(graph)
    colors = [-1] * num_vertices #This line initializes a list called colors with -1 as the initial value 
    #for each vertex. The value -1 indicates that no color has been assigned to a vertex yet.
    solution = []

    def solve(vertex):
        if vertex == num_vertices:
            return True

        for color in range(num_vertices):
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

    def print_solution():
        color_map = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
        for vertex in range(num_vertices):
            solution.append((vertex, color_map[colors[vertex]]))
        print("Vertex Colors:", solution)

    if solve(0):
        print_solution()
    else:
        print("No solution exists.")


# Example usage
num_vertices = int(input("Enter the number of vertices: "))
graph = [[] for _ in range(num_vertices)]
for vertex in range(num_vertices):
    neighbors = input(f"Enter the neighbors of vertex {vertex} (space-separated): ").split()
    graph[vertex] = [int(neighbor) for neighbor in neighbors]

solve_graph_coloring(graph)

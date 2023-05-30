import heapq

# Define the goal state
goal_state = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))

# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                row, col = divmod(state[i][j] - 1, 3)
                distance += abs(row - i) + abs(col - j)
    return distance

# Define the A* algorithm
def solve_8_puzzle(initial_state):
    open_set = []
    heapq.heappush(open_set, (heuristic(initial_state), initial_state))
    closed_set = set()
    g = {tuple(map(tuple, initial_state)): 0}
    parent = {tuple(map(tuple, initial_state)): None}

    while open_set:
        current_cost, current_state = heapq.heappop(open_set)

        if current_state == goal_state:
            # Goal state reached, backtrack to get the path
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent[current_state]
            return path[::-1]

        closed_set.add(current_state)

        # Generate successor states
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        for move in moves:
            new_state = [list(row) for row in current_state]
            row, col = next((i, j) for i, row in enumerate(current_state) for j, val in enumerate(row) if val == 0)
            new_row, new_col = row + move[0], col + move[1]

            # Check if the move is within the grid
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                new_state = tuple(map(tuple, new_state))

                if new_state not in closed_set:
                    new_cost = g[current_state] + 1
                    if new_state not in g or new_cost < g[new_state]:
                        g[new_state] = new_cost
                        f = new_cost + heuristic(new_state)
                        heapq.heappush(open_set, (f, new_state))
                        parent[new_state] = current_state

    # No solution found
    return None

# Example usage
'''initial_state = ((1, 2, 3),
                   (4, 0, 5),
                    (7, 8, 6))

solution = solve_8_puzzle(initial_state)'''
def get_user_input():
    print("Enter the initial state of the 8-puzzle:")
    initial_state = []
    for i in range(3):
        row = input("Enter row {} (space-separated values): ".format(i + 1)).split()
        row_values = tuple(map(int, row))
        initial_state.append(row_values)
    return tuple(initial_state)

solution = solve_8_puzzle(get_user_input())

if solution:
    print("Solution found!")
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
'''
o/p - 
G:\Ai programs>python astar.py
Enter the initial state of the 8-puzzle:
Enter row 1 (space-separated values): 1 2 3
Enter row 2 (space-separated values): 4 0 5
Enter row 3 (space-separated values): 6 7 8
Solution found!
(1, 2, 3)
(4, 0, 5)
(6, 7, 8)

(1, 2, 3)
(4, 5, 0)
(6, 7, 8)

(1, 2, 3)
(4, 5, 8)
(6, 7, 0)

(1, 2, 3)
(4, 5, 8)
(6, 0, 7)

(1, 2, 3)
(4, 5, 8)
(0, 6, 7)

(1, 2, 3)
(0, 5, 8)
(4, 6, 7)

(1, 2, 3)
(5, 0, 8)
(4, 6, 7)

(1, 2, 3)
(5, 6, 8)
(4, 0, 7)

(1, 2, 3)
(5, 6, 8)
(4, 7, 0)

(1, 2, 3)
(5, 6, 0)
(4, 7, 8)

(1, 2, 3)
(5, 0, 6)
(4, 7, 8)

(1, 2, 3)
(0, 5, 6)
(4, 7, 8)

(1, 2, 3)
(4, 5, 6)
(0, 7, 8)

(1, 2, 3)
(4, 5, 6)
(7, 0, 8)

(1, 2, 3)
(4, 5, 6)
(7, 8, 0)
'''

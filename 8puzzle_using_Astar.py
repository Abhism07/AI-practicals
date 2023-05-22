import heapq
goal_state = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                row, col = divmod(state[i][j] - 1, 3)
                distance += abs(row - i) + abs(col - j)
    return distance


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
    return None

initial_state = ((1, 0, 3),
                 (4, 2, 5),
                 (7, 8, 6))

solution = solve_8_puzzle(initial_state)

if solution:
    print("Solution found!")
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")

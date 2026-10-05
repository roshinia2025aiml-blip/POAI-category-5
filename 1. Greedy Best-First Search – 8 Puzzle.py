import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    """Manhattan Distance"""
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_index = GOAL.index(state[i])

            row1, col1 = divmod(i, 3)
            row2, col2 = divmod(goal_index, 3)

            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def greedy_bfs(start):
    queue = []
    heapq.heappush(queue, (heuristic(start), start))

    visited = set()
    parent = {start: None}

    while queue:

        h, current = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        print("Exploring:")
        print_puzzle(current)

        if current == GOAL:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        for next_state in get_neighbors(current):

            if next_state not in visited:

                if next_state not in parent:
                    parent[next_state] = current

                heapq.heappush(
                    queue,
                    (heuristic(next_state), next_state)
                )

    return None


# Initial state
start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

solution = greedy_bfs(start)

if solution:

    print("\nSolution Path:")

    for step, state in enumerate(solution):
        print("Step", step)
        print_puzzle(state)

else:
    print("No solution found.")

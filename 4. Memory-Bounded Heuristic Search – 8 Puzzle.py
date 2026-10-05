GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_index = GOAL.index(state[i])

            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(goal_index, 3)

            distance += abs(r1 - r2) + abs(c1 - c2)

    return distance


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
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


def search(path, g, threshold):

    current = path[-1]

    f = g + heuristic(current)

    if f > threshold:
        return f

    if current == GOAL:
        return True

    minimum = float("inf")

    for next_state in get_neighbors(current):

        if next_state not in path:

            path.append(next_state)

            result = search(path, g + 1, threshold)

            if result is True:
                return True

            minimum = min(minimum, result)

            path.pop()

    return minimum


def ida_star(start):

    threshold = heuristic(start)

    path = [start]

    while True:

        result = search(path, 0, threshold)

        if result is True:
            return path

        if result == float("inf"):
            return None

        threshold = result


def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()


# Initial state
start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

solution = ida_star(start)

if solution:

    print("Solution Path:")

    for step, state in enumerate(solution):

        print("Step", step)
        print_puzzle(state)

else:
    print("No solution found.")

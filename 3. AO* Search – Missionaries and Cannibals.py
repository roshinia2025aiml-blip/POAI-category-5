from heapq import heappush, heappop

START = (3, 3, 1)
GOAL = (0, 0, 0)


def valid(state):
    m, c, boat = state

    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    rm = 3 - m
    rc = 3 - c

    if rm > 0 and rm < rc:
        return False

    return True


def successors(state):
    m, c, boat = state

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    result = []

    for dm, dc in moves:

        if boat == 1:
            new_state = (m - dm, c - dc, 0)
        else:
            new_state = (m + dm, c + dc, 1)

        if valid(new_state):
            result.append(new_state)

    return result


def ao_star():

    queue = []

    heappush(queue, (0, START, [START]))

    visited = set()

    while queue:

        cost, state, path = heappop(queue)

        if state in visited:
            continue

        visited.add(state)

        print("Exploring:", state)

        if state == GOAL:
            return path

        for next_state in successors(state):

            if next_state not in visited:

                new_path = path + [next_state]

                heappush(
                    queue,
                    (len(new_path), next_state, new_path)
                )

    return None


solution = ao_star()

if solution:

    print("\nSolution Path:")

    for state in solution:
        print(state)

else:
    print("No solution found.")

from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()
        print(f"Current State: Jug1 = {x}, Jug2 = {y}")

        if x == target or y == target:
            print(f"Solution found: Jug1 = {x}, Jug2 = {y}")
            return True

        next_states = [
            (jug1, y),
            (x, jug2),
            (0, y),
            (x, 0),
            (min(x + y, jug1), y - (min(x + y, jug1) - x)),
            (x - (min(x + y, jug2) - y), min(x + y, jug2))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)

    print("No solution exists.")
    return False

jug1_capacity = int(input("Enter the jug 1 capacity: "))
jug2_capacity = int(input("Enter the jug 2 capacity: "))
target_amount = int(input("Enter the target amount: "))

water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)

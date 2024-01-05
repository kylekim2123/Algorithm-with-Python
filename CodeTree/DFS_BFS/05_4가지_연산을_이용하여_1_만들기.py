from collections import deque


def bfs():
    queue = deque([(n, 0)])
    visited = {n}

    while queue:
        number, counts = queue.popleft()
        counts += 1

        for d in delta:
            if d >= 2 and number % d == 0:
                next_number = number // d
            elif d <= 1:
                next_number = number + d

            if next_number >= 1 and next_number not in visited:
                if next_number == 1:
                    return counts

                visited.add(next_number)
                queue.append((next_number, counts))


n = int(input())
delta = [1, -1, 2, 3]

if n == 1:
    print(0)
else:
    print(bfs())

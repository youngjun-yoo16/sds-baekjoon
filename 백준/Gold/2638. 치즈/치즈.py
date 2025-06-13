from collections import deque

def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    cheese = deque()
    count = 0
    direction = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    visited = set([])

    def find_initial_vulnerable_cheese(outside_air):
        nonlocal cheese, count
        initial_vulnerable_cheese = deque()

        for r in range(N):
            for c in range(M):
                if grid[r][c]:
                    cheese.append((r, c))
                    count += 1
                    air = 0
                    for dr, dc in direction:
                        nr, nc = r + dr, c + dc
                        # 외부 공기에 접촉 했는지 확인
                        if (nr, nc) in outside_air:
                            air += 1
                    if air >= 2:
                        initial_vulnerable_cheese.append((r, c))

        return initial_vulnerable_cheese

    def find_outside_air():
        q = deque([(0, 0), (0, M - 1), (N - 1, 0), (N - 1, M - 1)])
        outside_air = {(0, 0), (0, M - 1), (N - 1, 0), (N - 1, M - 1)}

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and not grid[nr][nc] and (nr, nc) not in outside_air:
                        q.append((nr, nc))
                        outside_air.add((nr, nc))

        return outside_air

    def bfs():
        nonlocal hours, count
        while vulnerable_cheese and count:
            for _ in range(len(vulnerable_cheese)):
                r, c = vulnerable_cheese.popleft()
                visited.add((r, c))
                grid[r][c] = 0
                count -= 1

            outside_air = find_outside_air()

            for r, c in cheese:
                if (r, c) not in visited:
                    air = 0
                    for dr, dc in direction:
                        nr, nc = r + dr, c + dc
                        if (nr, nc) in outside_air:
                            air += 1
                    if air >= 2:
                        vulnerable_cheese.append((r, c))

            hours += 1

    hours = 0

    outside_air = find_outside_air()
    vulnerable_cheese = find_initial_vulnerable_cheese(outside_air)
    bfs()

    print(hours)

if __name__ == '__main__':
    main()
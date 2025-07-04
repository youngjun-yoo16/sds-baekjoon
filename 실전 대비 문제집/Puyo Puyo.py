from collections import deque


def main():
    grid = [list(input()) for _ in range(12)]
    N, M = len(grid), len(grid[0])

    def burst(l, r, c):
        q = deque([(r, c)])
        visited = {(r, c)}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == l:
                    grid[nr][nc] = '.'
                    q.append((nr, nc))
                    visited.add((nr, nc))

    def find_and_burst():
        nonlocal found
        visited = set([])

        def bfs(letter, r, c):
            nonlocal found, visited

            q = deque([(r, c)])
            visited.add((r, c))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            num_letter = 1

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == letter and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        num_letter += 1

            if num_letter >= 4:
                return letter, r, c

            return -1, -1, -1

        for r in range(N):
            for c in range(M):
                if grid[r][c] != '.' and (r, c) not in visited:
                    l, i, j = bfs(grid[r][c], r, c)
                    if l != -1:
                        found = True
                        burst(l, i, j)

    def fall_down():
        for i in range(N - 1):
            for j in range(M):
                p = i
                while p >= 0 and grid[p][j] != '.' and grid[p + 1][j] == '.':
                    grid[p][j], grid[p + 1][j] = grid[p + 1][j], grid[p][j]
                    p -= 1

    found, count = False, 0
    while True:
        find_and_burst()

        if not found: break

        fall_down()

        count += 1
        found = False

    print(count)

if __name__ == '__main__':
    main()
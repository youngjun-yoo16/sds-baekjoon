from collections import deque
from itertools import combinations

def main():
    N, M, G, R = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]
    fertile_land = deque(((i, j) for i in range(N) for j in range(M) if grid[i][j] == 2))

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    max_flowers = 0

    # 3: Green, 4: Red, 5: Flower
    for comb in combinations(fertile_land, G + R):
        for comb2 in combinations(comb, G):
            temp_grid = [row[:] for row in grid]
            green = deque()
            for r, c in comb2:
                temp_grid[r][c] = 3
                visited[r][c] = 0
                green.append((r, c, 0))

            red = deque()
            for r, c in comb:
                if (r, c) not in comb2:
                    temp_grid[r][c] = 4
                    visited[r][c] = 0
                    red.append((r, c, 0))

            while True:
                if not green and not red:
                    break

                new_green = deque()
                for r, c, s in green:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < M and temp_grid[nr][nc] == 1 or \
                            0 <= nr < N and 0 <= nc < M and temp_grid[nr][nc] == 2:
                            new_green.append((nr, nc, s + 1))
                            temp_grid[nr][nc] = 3
                            visited[nr][nc] = s + 1
                green = new_green.copy()

                new_red = deque()
                for r, c, s in red:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < M:
                            if temp_grid[nr][nc] == 1 or temp_grid[nr][nc] == 2:
                                new_red.append((nr, nc, s + 1))
                                temp_grid[nr][nc] = 4
                                visited[nr][nc] = s + 1
                            # Arrived at the same time
                            if temp_grid[nr][nc] == 3 and visited[nr][nc] == s + 1:
                                # Flower blooms
                                temp_grid[nr][nc] = 5
                                if green:
                                    green.remove((nr, nc, s + 1))
                red = new_red.copy()

            num_flowers = sum(1 for i in range(N) for j in range(M) if temp_grid[i][j] == 5)
            max_flowers = max(max_flowers, num_flowers)

    print(max_flowers)


if __name__ == '__main__':
    main()
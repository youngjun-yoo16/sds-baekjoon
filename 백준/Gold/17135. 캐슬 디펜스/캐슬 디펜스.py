import sys
from collections import deque
from itertools import combinations

def main():
    input = sys.stdin.readline
    N, M, D = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # Directions for BFS: left, up, right
    dirs = [(0, -1), (-1, 0), (0, 1)]

    def simulate(archers):
        # make a fresh copy of the battlefield
        temp = [row[:] for row in matrix]
        total_kills = 0

        # “Move” the enemies down by imagining archers rising from row N to row 0
        for turn_row in range(N - 1, -1, -1):
            targets = set()

            # each archer fires once this turn
            for a_col in archers:
                visited = [[False]*M for _ in range(N)]
                dq = deque([(turn_row, a_col, 1)])
                visited[turn_row][a_col] = True

                while dq:
                    x, y, dist = dq.popleft()
                    if temp[x][y] == 1:
                        targets.add((x, y))
                        break
                    if dist < D:
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                                visited[nx][ny] = True
                                dq.append((nx, ny, dist + 1))

            # eliminate all distinct targets and count them
            for x, y in targets:
                temp[x][y] = 0
            total_kills += len(targets)

        return total_kills

    answer = 0
  
    for archers in combinations(range(M), 3):
        answer = max(answer, simulate(archers))

    print(answer)

if __name__ == "__main__":
    main()
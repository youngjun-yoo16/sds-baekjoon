from collections import deque

def main():
    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    ripe = deque()
    unripe = 0

    for r in range(N):
        for c in range(M):
            if box[r][c] == 1:
                ripe.append((r, c))
            elif box[r][c] == 0:
                unripe += 1

    def bfs():
        nonlocal unripe, days
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while ripe and unripe:
            for _ in range(len(ripe)):
                r, c = ripe.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
                        ripe.append((nr, nc))
                        box[nr][nc] = 1
                        unripe -= 1
            days += 1

    days = 0
    bfs()

    print(days) if not unripe else print(-1)

if __name__ == '__main__':
    main()
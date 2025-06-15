from collections import deque

def main():
    K = int(input())
    W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    horse_directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    normal_directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    q = deque(([(0, 0, 0, K)]))
    visited = {(0, 0, K)}

    while q:
        r, c, s, k = q.popleft()

        if (r, c) == (H - 1, W - 1):
            print(s)
            return

        # Normal 4-directional moves
        for dr, dc in normal_directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and not grid[nr][nc] and (nr, nc, k) not in visited:
                q.append((nr, nc, s + 1, k))
                visited.add((nr, nc, k))
        
        # Horse moves if k > 0
        if k > 0:
            for dr, dc in horse_directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and not grid[nr][nc] and (nr, nc, k - 1) not in visited:
                    q.append((nr, nc, s + 1,k - 1))
                    visited.add((nr, nc, k - 1))

    print(-1)

if __name__ == '__main__':
    main()
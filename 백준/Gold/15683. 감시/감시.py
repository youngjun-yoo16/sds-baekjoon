from collections import defaultdict

def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    cctvs = []
    num_cctv = 0
    walls = 0
    for r in range(N):
        for c in range(M):
            if not grid[r][c]: continue
            if grid[r][c] == 6:
                walls += 1
            else:
                cctvs.append((grid[r][c], r, c))
                num_cctv += 1

    min_area = float('inf')

    answer = [
        [1, '#', '#', '#', '#', '#'],
        [0, 1, '#', '#', '#', '#'],
        [0, 0, 1, '#', '#', '#'],
        ['#', '#', '#', 1, 0, 0],
        ['#', '#', '#', '#', 0, 0],
        ['#', '#', '#', '#', '#', 1]
    ]

                        # [East], [West], [North], [South]
    directions = { 1 : [[(0, 1)], [(0, -1)], [(-1, 0)], [(1, 0)]],
                        # [East, West], [North, South]
                   2 : [[(0, 1), (0, -1)], [(-1, 0), (1, 0)]],
                        # [[East, North], [East, South],
                        #  [West, South], [West, North]]
                   3 : [[(0, 1), (-1, 0)], [(0, 1), (1, 0)],
                         [(0, -1), (1, 0)], [(0, -1), (-1, 0)]],
                        # [[East, North, West], [North, West, South],
                        #  [West, South, East], [South, East, North]]
                   4 : [[(0, 1), (-1, 0), (0, -1)], [(-1, 0), (0, -1), (1, 0)],
                         [(0, -1), (1, 0), (0, 1)], [(1, 0), (0, 1), (-1, 0)]],
                        # [East, West, North, South]
                   5 : [[(0, 1), (0, -1), (-1, 0), (1, 0)]] }

    def mark(r, c, dr, dc):
        nr, nc = r, c

        while True:
            nr += dr
            nc += dc
            if not(0 <= nr < N and 0 <= nc < M): break
            # 벽을 만났 거나 다른 cctv가 이미 탐색 했던 곳을 만났을 때
            if grid[nr][nc] == 6: break
            # 다른 cctv를 만났을 때
            if grid[nr][nc] in range(1, 6): continue
            grid[nr][nc] = '#'
            visited[nr][nc] += 1

    def unmark(r, c, dr, dc):
        nr, nc = r, c

        while True:
            nr += dr
            nc += dc
            if not (0 <= nr < N and 0 <= nc < M): break
            # 벽을 만났 거나 다른 cctv가 이미 탐색 했던 곳을 만났을 때
            if grid[nr][nc] == 6: break
            # 다른 cctv를 만났을 때
            if grid[nr][nc] == '#':
                visited[nr][nc] -= 1
                if visited[nr][nc] <= 0:
                    grid[nr][nc] = 0

    def get_num_blind_spots():
        spots = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 0:
                    spots += 1

        return spots

    def backtrack(cctv_idx):
        nonlocal min_area, num_cctv

        if cctv_idx == num_cctv:
            min_area = min(min_area, get_num_blind_spots())
            return

        cctv_num, r, c = cctvs[cctv_idx]
        for direction in directions[cctv_num]:
            for dr, dc in direction:
                mark(r, c, dr, dc)

            backtrack(cctv_idx + 1)

            for dr, dc in direction:
                unmark(r, c, dr, dc)

    backtrack(0)

    print(min_area)

if __name__ == '__main__':
    main()
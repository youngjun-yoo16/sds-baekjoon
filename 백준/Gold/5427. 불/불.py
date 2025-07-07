from collections import deque

def main():
    T = int(input())

    for _ in range(T):
        M, N = map(int, input().split())
        grid = [list(input()) for _ in range(N)]
        fire = deque(((i, j) for i in range(N) for j in range(M) if grid[i][j] == '*'))
        pos = deque(((i, j, 1) for i in range(N) for j in range(M) if grid[i][j] == '@'))
        user_r, user_c, _ = pos[0]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        escaped = False

        while True:
            # No more position to escape
            if not pos:
                break

            # Escape condition (border)
            for r, c, s in pos:
                if r == N - 1 or r == 0 or c == M - 1 or c == 0:
                    print(s)
                    escaped = True
                    break

            # Break while loop
            if escaped: break

            # Spread all fires (flood-fill)
            new_fire = deque([])
            for i in range(len(fire)):
                fr, fc = fire[i]
                for dr, dc in directions:
                    nr, nc = fr + dr, fc + dc
                    if ((0 <= nr < N and 0 <= nc < M and grid[nr][nc] == '@') or
                            (0 <= nr < N and 0 <= nc < M and grid[nr][nc] == '.')):
                        grid[nr][nc] = '*'
                        new_fire.append((nr, nc))
            fire = new_fire.copy()

            # Escape
            new_pos = deque([])
            for i in range(len(pos)):
                pr, pc, ps = pos[i]
                for dr, dc in directions:
                    nr, nc = pr + dr, pc + dc
                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == '.':
                        grid[nr][nc] = '@'
                        new_pos.append((nr, nc, ps + 1))
            pos = new_pos.copy()

        #     for row in grid:
        #         print(*row, sep='')
        #
        #     print("---------------")
        #
        #
        # for row in grid:
        #     print(*row, sep='')
        #
        # print("---------------")

        if not escaped:
            print("IMPOSSIBLE")

if __name__ == '__main__':
    main()
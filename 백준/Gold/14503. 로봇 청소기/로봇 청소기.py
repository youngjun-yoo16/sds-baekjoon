from collections import deque

def main():
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # East, north, west, south
    # 90 degrees anticlockwise - (idx + 1) % 4
    # 90 degrees clockwise - (idx + 3) % 4
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    # 0: north, 1: east, 2: south, 3: west
    directions_map = { 0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1) }

    def clean(i, j):
        nonlocal directions, directions_map, d
        stack = [(i, j)]
        grid[i][j] = 2

        while stack:
            i, j = stack.pop()
            cur_dir = directions_map[d]
            # Rotate 90 degrees anticlockwise until there's an uncleaned cell in front.
            for _ in range(len(directions)):
                idx = (directions.index(cur_dir) + 1) % 4
                xr, xc = i + directions[idx][0], j + directions[idx][1]
                d = [key for key, val in directions_map.items() if val == directions[idx]][0]
                # Change the direction
                cur_dir = directions_map[d]
                # Found uncleaned cell
                if 0 <= xr < N and 0 <= xc < M and not grid[xr][xc]:
                    grid[xr][xc] = 2
                    stack.append((xr, xc))
                    break
            else:
                # All adjacent cells are already cleaned
                # Go one cell backward
                xr, xc = i - cur_dir[0], j - cur_dir[1]
                # Stop cleaning when there's a wall
                if grid[xr][xc] == 1: return
                # If not, start again from one cell backward
                stack.append((xr, xc))

    clean(r, c)
    print(sum(1 for r in range(N) for c in range(M) if grid[r][c] == 2))

if __name__ == '__main__':
    main()
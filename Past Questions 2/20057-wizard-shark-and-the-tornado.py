from collections import deque

def main():
    N = int(input().strip())
    grid = [list(map(int, input().strip().split(" "))) for _ in range(N)]

    # Each tuple = (row offset, col offset, percentage)
    left = [(-1, 0, 7), (1, 0, 7), (-2, 0, 2), (2, 0, 2), 
            (1, 1, 1), (-1, 1, 1), (1, -1, 10), (-1, -1, 10), 
            (0, -2, 5), (0, -1, 0)]
    down = [(0, -1, 7), (0, 1, 7), (0, -2, 2), (0, 2, 2),
            (-1, -1, 1), (-1, 1, 1), (1, -1, 10), (1, 1, 10),
            (2, 0, 5), (1, 0, 0)]
    right = [(r, -c, percent) for r, c, percent in left]
    up = [(-r, c, percent) for r, c, percent in down]

    # Tornado starts from the center of the grid
    r = c = N // 2

    # Direction vectors: left, down, right, up
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # Number of moves in the current spiral direction
    rotation = 1
    # Direction index (rotates from 0 to 3)
    count = 0
    # Sand that goes out of bounds
    res = 0

    def spread(r, c, direction):
        nonlocal res
        toal_amount_spread = 0
        original_amount = grid[r][c]

        for i in range(len(direction)):
            dr, dc, percent = direction[i]
            nr, nc = r + dr, c + dc
            
            # Calculate amount to spread
            amount_spread = int(original_amount * (percent / 100)) 

            # Calculate Alpha: remaining sand after all spreads
            if i == len(direction) - 1:
                alpha = original_amount - toal_amount_spread
                amount_spread = alpha

            # Out of bounds -> add to result
            if not ((0 <= nr < N) and (0 <= nc < N)):
                res += amount_spread
            else:
                grid[nr][nc] += amount_spread
            
            grid[r][c] -= amount_spread
            toal_amount_spread += amount_spread

    flag = True
    while flag:
        for _ in range(rotation):
            r += dx[count % 4] 
            c += dy[count % 4]

            # Left 
            if count % 4 == 0:
                spread(r, c, left)

            # Down
            elif count % 4 == 1:
                spread(r, c, down)
            
            # Right
            elif count % 4 == 2:
                spread(r, c, right)

            # Up
            else:
                spread(r, c, up)
            
            # Reached the end
            if (r, c) == (0, 0):
                flag = False
                break

        count += 1

        # Increase rotation steps after every two direction changes
        rotation = rotation + 1 if not count % 2 else rotation

    print(res)

if __name__=="__main__":
    main()
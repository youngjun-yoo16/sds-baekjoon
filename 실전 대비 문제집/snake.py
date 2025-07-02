from collections import deque

def main():
    N = int(input())
    K = int(input())
    q = deque([tuple(map(lambda e: int(e) - 1, input().split())) for _ in range(K)])
    L = int(input())
    directions_info = [tuple(input().split()) for _ in range(L)]

    snake = deque([(0, 0)])
    time = 0
    grid = [[0] * N for _ in range(N)]
    for r, c in q: grid[r][c] = 1

    # East, north, west, south
    # 90 degrees anticlockwise - (idx + 1) % 4
    # 90 degrees clockwise - (idx + 3) % 4
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    # Starts with east
    d = 0

    def rotate(direction):
        nonlocal d

        # Rotate 90 degrees right
        if direction == 'D':
            d = (d + 3) % 4
        # Rotate 90 degrees left
        else:
            d = (d + 1) % 4

    while True:
        # Position of the snake's head
        r, c = snake[-1]

        # Check if it's time to rotate
        if directions_info and time == int(directions_info[0][0]):
            rotate(directions_info[0][1])
            directions_info.pop(0)

        dr, dc = directions[d]
        nr, nc = r + dr, c + dc

        # Game over
        if not(0 <= nr < N and 0 <= nc < N) or (nr, nc) in snake:
            break

        # Position of the snake's new head
        snake.append((nr, nc))

        # Apple
        if grid[nr][nc]:
            grid[nr][nc] = 0
        # No apple
        else:
            # Shrink it's tail
            snake.popleft()

        time += 1

    print(time + 1)

if __name__ == '__main__':
    main()
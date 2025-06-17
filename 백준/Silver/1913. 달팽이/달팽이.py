def main():
    N = int(input())
    M = int(input())
    grid = [[0] * N for _ in range(N)]
    grid[N // 2][N // 2] = 1

    rotation = 0
    num = 2
    r, c = N // 2, N // 2
    x, y = N // 2, N // 2

    # Up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    flag = True
    while flag:
        for dr, dc in directions:
            for _ in range(rotation // 2 + 1):
                if num == N ** 2 + 1:
                    flag = False
                    break

                r += dr
                c += dc
                grid[r][c] = num

                if num == M:
                    x, y = r, c

                num += 1

            rotation += 1

        if not flag:
            break

    for row in grid:
        print(*row)

    print(x + 1, y + 1)

if __name__ == '__main__':
    main()
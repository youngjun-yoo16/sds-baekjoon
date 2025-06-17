def main():
    M, n = map(int, input().split())
    orders = [[] for _ in range(n)]

    for i in range(n):
        order, amount = input().split()
        orders[i].append(order)
        orders[i].append(int(amount))

    # 동 북 서 남
    # 왼 쪽으로 90도 할 때마다 (idx + 1) % 4
    # 오른 쪽으로 90도 할 때마다 (idx - 1 + 4) % 4
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    idx = 0
    r, c = M - 1, 0

    for order, amount in orders:
        dr, dc = directions[idx]
        if order == 'TURN':
            # 왼 쪽으로 90도
            if not amount:
                idx = (idx + 1) % 4
            # 오른 쪽으로 90도
            else:
                idx = (idx - 1 + 4) % 4
        # MOVE
        else:
            for i in range(amount):
                r += dr
                c += dc

            if not(0 <= r < M and 0 <= c < M):
                print(-1)
                return

    print(c, M - r - 1)

if __name__ == '__main__':
    main()
from collections import deque
from itertools import combinations


def main():
    N, M = map(int, input().split())
    city = list(list(map(int, input().split(' '))) for _ in range(N))
    houses = deque()
    chickens = deque()

    for r in range(N):
        for c in range(N):
            if city[r][c] == 1:
                houses.append((r, c))
            elif city[r][c] == 2:
                chickens.append((r, c))

    res = float('inf')
    for comb in combinations(chickens, M):
        temp_chickens = chickens.copy()
        for r, c in chickens:
            if (r, c) not in comb:
                temp_chickens.remove((r, c))

        total_dist = 0
        for r, c in houses:
            min_dist = float('inf')
            for r2, c2 in temp_chickens:
                min_dist = min(min_dist, abs(r2 - r) + abs(c2 - c))
            total_dist += min_dist

        res = min(res, total_dist)

    print(res)

if __name__ == '__main__':
    main()
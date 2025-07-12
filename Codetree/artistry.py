'''
1. 그룹 만들기
    - 동일한 숫자가 상하좌우로 인접해 있는 경우 동일한 그룹임
2. 예술 점수 구하기
    - 두 그룹의 조화로움 값: (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값
    x 그룹 a와 그룹 b가 서로 맞닿아 있 변의 수
    - 초기 예술 점수는 맞닿아 있는 모든 그룹의 조화로움 값을 다 더한 수
3. 회전
    - 정중에 십자 모양과 그 외 부분으로 나누어 진행
    - 십자 모양은 통째로 90도 반시계 방향 회전
    - 십자 모양 제외한 4개의 정사각형은 각각 개별적으로 시계 방향으로 90도 회전
4. 회전 후 예술 점수 구하 (1회전 후 예술 점수)

구해야 되는 것:
1. 초기 예술 점수
2. 1회전 후 예술 점수
3. 2회전 후 예술 점수
4. 3회전 후 예술 점수
'''
from collections import defaultdict, deque


def main():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    def find_group():
        groups = defaultdict(list)
        visited = set([])
        group_num = 1

        def bfs(r, c, num):
            nonlocal visited
            group = [(r, c)]
            visited.add((r, c))
            q = deque([(r, c)])
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == num:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        group.append((nr, nc))

            return group

        for r in range(n):
            for c in range(n):
                if (r, c) not in visited:
                    g = bfs(r, c, grid[r][c])
                    groups[group_num] = g
                    group_num += 1

        return groups

    def find_pairs(groups):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pairs = defaultdict(int)

        for key, val in groups.items():
            for r, c in val:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not(0 <= nr < n and 0 <= nc < n): continue
                    for k, v in groups.items():
                        # Skip the same group
                        if k == key: continue
                        # Find combinations
                        if (nr, nc) in v:
                            if (k, key) in pairs:
                                continue
                            else:
                                pairs[(key, k)] += 1

        return pairs

    def find_harmony_score(pair, num_sides, groups):
        num_cells_group_1, num_cells_group_2 = len(groups[pair[0]]), len(groups[pair[1]])
        group1_val = grid[groups[pair[0]][0][0]][groups[pair[0]][0][1]]
        group2_val = grid[groups[pair[1]][0][0]][groups[pair[1]][0][1]]

        harmony_score = (num_cells_group_1 + num_cells_group_2) * group1_val * group2_val * num_sides

        return harmony_score

    def find_art_score(pairs, groups):
        total_score = 0

        for key, val in pairs.items():
            total_score += find_harmony_score(key, val, groups)

        return total_score

    def rotate():
        nonlocal grid
        new_grid = [[0] * n for _ in range(n)]
        center = n // 2
        len_square = n - center - 1
        cross = set([])

        for i in range(n):
            for j in range(n):
                if j == center or i == center:
                    cross.add((i, j))

        def rotate_square(si, sj, length):
            for i in range(si, si + length):
                for j in range(sj, sj + length):
                    oi, oj = i - si, j - sj
                    ri, rj = oj, length - oi - 1
                    new_grid[si + ri][sj + rj] = grid[i][j]

        # 십자 모양 회전
        for i in range(n):
            for j in range(n):
                # 90도 반시계 방향
                if (i, j) in cross:
                    new_grid[n - j - 1][i] = grid[i][j]

        # 4개의 정사각형 회전
        rotate_square(0, 0, len_square)
        rotate_square(0, center + 1, len_square)
        rotate_square(center + 1, 0, len_square)
        rotate_square(center + 1, center + 1, len_square)

        grid = new_grid

    total_score = 0
    for _ in range(4):
        g = find_group()
        p = find_pairs(g)
        total_score += find_art_score(p, g)
        rotate()

    print(total_score)


if __name__ == '__main__':
    main()


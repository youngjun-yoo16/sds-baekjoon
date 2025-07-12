'''
1. 성장
    - 인접한 상하좌우에 나무가 있는 칸의 개수만큼 성장
2. 번식
    - 인접한 상하좌우에 나무/벽/제초제가 모두 없는 칸의 개수 구하기
    - 나무 그루 수에서 번식 가능한 칸의 개수만큼 나누어진 그루 수 만큼 번식 (나머지는 버림)
    - 모든 나무에서 동시에 번식 (temp_grid 만들기 필수; 번식이 겹치는 칸은 더하기)
3. 제초제 뿌리기
    - 4개의 대각선 방향으로 k칸만큼 전파됨
        - 단 중간에 벽이 있거나 나무가 아예 없는 칸이 있는 경우 그 칸 까지만 뿌려지고 그 이후는 X
    - c년간 제초제가 남아있고 c + 1년째가 되면 사라짐
    - 제초제가 뿌려진 곳에 다시 제초제가 뿌려지면 새로 뿌려진 해로부터 c년동안 제초제가 유지됨
    - 나무가 가장 많이 박멸되는 칸에 제초제 뿌려야됨
        - 동일한 칸이 있는 경우 행과 열이 작은 순서대로 선택
4. m년간 반복
    - 총 박멸한 나무 수 구하기
'''


def main():
    n, m, k, c = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    pesticides = [[0] * n for _ in range(n)]
    trees = set(((i, j) for i in range(n) for j in range(n) if grid[i][j] > 0))
    walls = list(((i, j) for i in range(n) for j in range(n) if grid[i][j] == -1))

    def grow():
        nonlocal trees
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r, c in trees:
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) in trees:
                    count += 1
            grid[r][c] += count

    def reproduce():
        nonlocal grid, pesticides, trees, walls
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        new_grid = [r[:] for r in grid]
        new_trees = []

        for r, c in trees:
            count = 0
            possible_cells = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < n): continue
                if pesticides[nr][nc] != 0: continue
                if (nr, nc) in walls or (nr, nc) in trees: continue
                count += 1
                possible_cells.append((nr, nc))

            if count:
                num_reproduce = grid[r][c] // count
                if num_reproduce:
                    for x, y in possible_cells:
                        new_grid[x][y] += num_reproduce
                        new_trees.append((x, y))

        grid = new_grid
        trees.update(new_trees)

    def spread_pesticides():
        nonlocal grid, pesticides, trees, walls, c
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        def find_tree_to_spread():
            nonlocal directions, k
            kill = [r[:] for r in grid]

            max_kill_count = 0
            for r, c in trees:
                kill_count = 0
                for dr, dc in directions:
                    for i in range(1, k + 1):
                        xr, xc = r + dr * i, c + dc * i
                        if not (0 <= xr < n and 0 <= xc < n): break
                        if (xr, xc) in walls or not grid[xr][xc]: break
                        kill_count += grid[xr][xc]
                kill[r][c] += kill_count
                max_kill_count = max(max_kill_count, kill[r][c])

            for r in range(n):
                for c in range(n):
                    if kill[r][c] == max_kill_count:
                        return max_kill_count, r, c

            return None, None, None

        count, x, y = find_tree_to_spread()

        if count:
            grid[x][y] = 0
            pesticides[x][y] = c
            trees.remove((x, y))
            for dr, dc in directions:
                for i in range(1, k + 1):
                    xr, xc = x + dr * i, y + dc * i
                    if not (0 <= xr < n and 0 <= xc < n): break
                    if (xr, xc) in walls or (xr, xc) not in trees:
                        pesticides[xr][xc] = c
                        break
                    grid[xr][xc] = 0
                    pesticides[xr][xc] = c
                    trees.remove((xr, xc))

        return count

    def remove_pesticides():
        for r in range(n):
            for c in range(n):
                if pesticides[r][c]:
                    pesticides[r][c] -= 1

    total_dead_trees = 0
    for _ in range(m):
        grow()
        reproduce()
        remove_pesticides()
        total_dead_trees += spread_pesticides()

    print(total_dead_trees)


if __name__ == '__main__':
    main()

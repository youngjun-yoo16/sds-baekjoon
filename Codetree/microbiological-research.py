from collections import defaultdict, deque
from copy import deepcopy

def main():
    N, Q = map(int, input().split())
    locations = [list(map(int, input().split())) for _ in range(Q)]
    grid = [[0] * N for _ in range(N)]

    def set_vertical_sizes():
        nonlocal vertical_sizes
        vertical_sizes.clear()

        for c in range(N):
            empty_spaces = 0
            start_r = start_c = None
            for r in range(N - 1, -1, -1):
                if not grid[r][c]:
                    empty_spaces += 1
                    if not start_r and not start_c:
                        start_r, start_c = r, c
                    if empty_spaces and not r:
                        vertical_sizes[c].append((start_r, start_c, empty_spaces))
                else:
                    # AND로 할 시 둘 중 한 개라도 0이면 안됨 ex: (3, 0)
                    if start_r or start_c:
                        vertical_sizes[c].append((start_r, start_c, empty_spaces))
                        start_r = start_c = None
                        empty_spaces = 0

        # Sort dictionary based on the size of free spaces in each column
        for key, value_set in vertical_sizes.items():
            sorted_list = sorted(list(value_set), key=lambda x: (x[1], -x[0], x[2]))
            vertical_sizes[key] = sorted_list

    def get_separated_bacteria():
        def bfs(r, c, num):
            q = deque([(r, c)])
            visited.add((r, c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and grid[nx][ny] == num:
                        visited.add((nx, ny))
                        q.append((nx, ny))

        visited = set([])
        num_visited = set()
        divided_bacteria = set([])

        for r in range(N):
            for c in range(N):
                if grid[r][c] and (r, c) not in visited:
                    # These bacteria have been divided into 2 or more areas
                    if grid[r][c] in num_visited:
                        divided_bacteria.add(grid[r][c])
                    else:
                        num_visited.add(grid[r][c])
                        bfs(r, c, grid[r][c])

        return divided_bacteria

    def remove_bacteria(num):
        for r in range(N):
            for c in range(N):
                if grid[r][c] == num:
                    grid[r][c] = 0

        position_recorder.pop(num, None)
        sizes.pop(num, None)

    def can_fit(temp, num, y_diff):
        nonlocal grid

        x_diff = N - 1
        for n in range(N * 2):
            found = True
            for i in range(len(position_recorder[num])):
                new_x = position_recorder[num][i][0] + x_diff
                new_y = position_recorder[num][i][1] + y_diff
                if 0 <= new_x < N and 0 <= new_y < N:
                    if temp[new_x][new_y]:
                        found = False
                        break
                else:
                    found = False
                    break

            if found:
                return True, x_diff, y_diff

            x_diff -= 1

        return False, -1, -1

    def get_position(num, temp):
        organism_positions = position_recorder[num]  # Positions of this bacteria
        min_y = min(organism_positions[i][1] for i in range(len(organism_positions)))

        # Check if vertical space is large enough to store this bacteria
        for i in range(N):
            if not vertical_sizes[i]: continue
            for x, y, size in vertical_sizes[i]:
                y_diff = y - min_y
                possible, x_diff_final, y_diff_final = can_fit(temp, num, y_diff)
                if possible:
                    return x_diff_final, y_diff_final

        return None, None

    def move(num):
        nonlocal grid, flag, vertical_sizes

        if not flag:
            temp = [[0] * N for _ in range(N)]
            vertical_sizes.clear()
            for i in range(N):
                vertical_sizes[i].append((N - i - 1, i, N))
            flag = True
        else:
            temp = deepcopy(grid)

        x_diff, y_diff = get_position(num, temp)

        # 어디에도 둘 수 없음
        if x_diff is None and y_diff is None:
            remove_bacteria(num)
            set_vertical_sizes()
            return

        organism_positions = position_recorder[num]  # Positions of this bacteria

        for i in range(len(organism_positions)):
            new_x = position_recorder[num][i][0] + x_diff
            new_y = position_recorder[num][i][1] + y_diff

            position_recorder[num][i][0] = new_x
            position_recorder[num][i][1] = new_y

        for i, j in position_recorder[num]:
            temp[i][j] = num

        grid = [row[:] for row in temp]

        # Update vertical sizes of each x after moving the bacteria
        set_vertical_sizes()

    def get_area():
        adjacent_bacteria = set([])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(N):
            for c in range(N):
                if not grid[r][c]: continue
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < N and 0 <= nc < N): continue
                    if not grid[nr][nc]: continue
                    if grid[r][c] != grid[nr][nc]:
                        if (grid[r][c], grid[nr][nc]) in adjacent_bacteria or \
                                (grid[nr][nc], grid[r][c]) in adjacent_bacteria: continue
                        adjacent_bacteria.add((grid[r][c], grid[nr][nc]))

        total_area = 0
        for b1, b2 in adjacent_bacteria:
            total_area += sizes[b1] * sizes[b2]

        return total_area

    def fill_in():
        to_remove = []
        for y in range(y1, y2):
            for x in range(x1, x2):
                grid[N - y - 1][x] = organism_num
                position_recorder[organism_num].append([N - y - 1, x])
                sizes[organism_num] += 1

                # 잡아 먹히는 미생물 좌표 없애기
                for k, v in position_recorder.items():
                    if k == organism_num: continue
                    if [N - y - 1, x] in v:
                        v.remove([N - y - 1, x])
                        sizes[k] -= 1
                        if not sizes[k]:
                            to_remove.append(k)

        for b in to_remove:
            remove_bacteria(b)

    position_recorder = defaultdict(list)

    # Stores vertical size of each x position
    vertical_sizes = defaultdict(list)

    # Initialize vertical sizes
    set_vertical_sizes()

    # Size of each bacterias
    sizes = defaultdict(int)

    organism_num = 0

    for x1, y1, x2, y2 in locations:
        organism_num += 1
        fill_in()

        # 둘 이상의 영역으로 나눠진 미생물 제거
        bacterias_to_remove = get_separated_bacteria()
        for bacteria in bacterias_to_remove:
            remove_bacteria(bacteria)

        # Sort the sizes in descending order
        flag = False
        for key, val in sorted(sizes.items(), key=lambda x: x[1], reverse=True):
            move(key)

        print(get_area())

if __name__ == '__main__':
    main()

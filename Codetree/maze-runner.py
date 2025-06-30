from collections import deque, defaultdict

def main():
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    positions = deque([])
    visited = [[0] * N for _ in range(N)]

    for _ in range(M):
        r, c = map(lambda e: int(e) - 1, input().split())
        positions.append((r, c))
        visited[r][c] += 1

    exit_r, exit_c = map(lambda e: int(e) - 1, input().split())
    total_distance_moved = 0

    def move():
        nonlocal total_distance_moved, positions, visited
        temp_positions = positions.copy()

        # Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r, c in positions:
            # No more participants left in this cell
            if not visited[r][c]: continue
            # Continue if this position is an exit
            if (r, c) == (exit_r, exit_c): continue

            distance = abs(r - exit_r) + abs(c - exit_c)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                new_distance = abs(nr - exit_r) + abs(nc - exit_c)
                # Only move to positions w/ shorter distance to the exit
                if new_distance >= distance: continue
                # Out of range
                if not (0 <= nr < N and 0 <= nc < N): continue
                # Wall
                if grid[nr][nc]: continue
                # Exit - do not add the new position
                if (nr, nc) == (exit_r, exit_c):
                    visited[r][c] -= 1
                    temp_positions.remove((r, c))
                    total_distance_moved += 1
                    break
                # Set the previous position to be outdated
                visited[r][c] -= 1
                # Add new position to the list
                visited[nr][nc] += 1
                temp_positions.remove((r, c))
                temp_positions.append((nr, nc))
                total_distance_moved += 1
                break

        positions = temp_positions

    def rotate(si, sj, size):
        nonlocal exit_r, exit_c, grid, positions, visited

        temp = [row[:] for row in grid]
        temp_visited = [row[:] for row in visited]
        temp_exit_r, temp_exit_c = exit_r, exit_c
        new_positions = deque([])

        # Positions that are outside the matrix
        for r, c in positions:
            if not(si <= r < si + size) or not(sj <= c < sj + size):
                new_positions.append((r, c))
        found_exit  = False

        # Rotate 90° clockwise
        for i in range(si, si + size):
            for j in range(sj, sj + size):
                oi, oj = i - si, j - sj
                ri, rj = oj, size - 1 - oi
                # -1 for walls
                if grid[i][j]:
                    temp[si + ri][sj + rj] = grid[i][j] - 1
                # Exit
                elif (i, j) == (exit_r, exit_c):
                    # To prevent double rotation of exit
                    # Do not rotate exit when it's already rotated
                    if found_exit: continue
                    temp[si + ri][sj + rj] = grid[i][j]
                    temp_exit_r, temp_exit_c = si + ri, sj + rj
                    found_exit = True
                # Candidates
                else:
                    # Rotate positions
                    temp[si + ri][sj + rj] = grid[i][j]
                    if (i, j) in positions:
                        # There can be more than 1 candidate in this position.
                        # Use temp_visited here to record the initial number of participants in (i, j)
                        # Directly using visited would modify visited[i][j] during the iteration and make
                        # incorrect movement.
                        while temp_visited[i][j]:
                            new_positions.append((si + ri, sj + rj))
                            visited[i][j] -= 1
                            visited[si + ri][sj + rj] += 1
                            temp_visited[i][j] -= 1

        positions = new_positions
        grid = temp
        exit_r, exit_c = temp_exit_r, temp_exit_c

    def find_square():
        # Brute force: starts from 2 x 2 matrix
        for size in range(2, N + 1):
            for i in range(N - size + 1):
                for j in range(N - size + 1):
                    is_candidate, is_exit = False, False
                    for si in range(size):
                        for sj in range(size):
                            if (i + si, j + sj) in positions and visited[i + si][j + sj]:
                                is_candidate = True
                            if (i + si, j + sj) == (exit_r, exit_c):
                                is_exit = True
                            if is_candidate and is_exit:
                                rotate(i, j, size)
                                return

    def check():
        for r in range(N):
            for c in range(N):
                # There's still a candidate in the maze
                if visited[r][c]: return False
        # No candidate left in the maze
        return True

    for i in range(K):
        move()
        # Check if all participants escaped
        if check(): break
        find_square()

    print(total_distance_moved)
    print(exit_r + 1, exit_c + 1)

if __name__ == '__main__':
    main()

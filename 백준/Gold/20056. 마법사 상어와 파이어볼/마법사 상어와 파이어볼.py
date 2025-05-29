from collections import deque

def main():
    N, M, K = map(int, input().strip().split(" "))
    grid = [[deque() for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        r, c, m, s, d = map(int, input().strip().split(" "))
        grid[r - 1][c - 1].append((m, s, d))
    
    directions = { 0 : (-1, 0), 1 : (-1, 1), 2 : (0, 1), 3 : (1, 1), 
                  4 : (1, 0), 5 : (1, -1), 6 : (0, -1), 7 : (-1, -1)}

    for _ in range(K):
        multiple_fireballs_positions = set()
        # Temporary grid for after-move state
        temp = [[deque() for _ in range(N)] for _ in range(N)]
        # Move all fireballs
        for r in range(N):
            for c in range(N):
                for _ in range(len(grid[r][c])):
                    m, s, d = grid[r][c].popleft()
                    nr, nc = (r + directions[d][0] * s) % N, (c + directions[d][1] * s) % N
                    if nr < 0:
                        nr += N
                    if nc < 0:
                        nc += N
                    temp[nr][nc].append((m, s, d))
                    # Mark positions if multiple fireballs end up in the same cell
                    if len(temp[nr][nc]) >= 2:
                        multiple_fireballs_positions.add((nr, nc))

        # Update the main grid after all movements
        grid = [row[:] for row in temp]

        # Merge and split fireballs at positions with multiple fireballs
        for r, c in multiple_fireballs_positions:
            total_m = total_s = num_fireballs = 0
            dirs = []

            # Aggregate fireball properties
            for _ in range(len(grid[r][c])):
                m, s, d = grid[r][c].popleft()
                total_m += m
                total_s += s
                num_fireballs += 1
                dirs.append(d)

            # Compute new mass and speed
            new_m = total_m // 5
            new_s = total_s // num_fireballs

            # Only split fireballs if mass > 0
            if new_m:
                is_odd = is_even = False
                even_directions = [0, 2, 4, 6]
                odd_directions = [1, 3, 5, 7]

                # Check parity of directions
                for d in dirs:
                    if not d % 2:
                        is_even = True
                    else:
                        is_odd = True

                # If both odd and even directions present -> use odd directions
                if is_even and is_odd:
                    for d in odd_directions:
                        grid[r][c].append((new_m, new_s, d))
                # All directions have same parity -> use even directions
                else:
                    for d in even_directions:
                        grid[r][c].append((new_m, new_s, d))
    
    res = 0
    for r in range(N):
        for c in range(N):
            for m, _, _ in grid[r][c]:
                res += m
    
    print(res)

if __name__=="__main__":
    main()
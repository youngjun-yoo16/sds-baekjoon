from collections import deque

def main():
    M, N = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(M)]
    start_r, start_c, start_d = map(int, input().split())
    dest_r, dest_c, dest_d = map(int, input().split())

    # East, west, north, south
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    start_r -= 1
    start_c -= 1
    dest_r -= 1
    dest_c -= 1

    q = deque([(start_r, start_c, start_d, 0)])
    visited = {(start_r, start_c, start_d)}
    res = float('inf')

    while q:
        r, c, d, steps = q.popleft()
      
        if (r, c, d) == (dest_r, dest_c, dest_d):
            print(steps)
            return
        
        # Try moving forward 1 to 3 steps
        dr, dc = directions[d - 1]
        for i in range(1, 4):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < M and 0 <= nc < N): break
            # Can't pass through or stop on a wall
            if grid[nr][nc]: break
            if (nr, nc, d) not in visited:
                visited.add((nr, nc, d))
                q.append((nr, nc, d, steps + 1))
        
        # Try changing directions
        for new_d in range(1, 5):
            if new_d == d or (r, c, new_d) in visited: continue
            # Determine rotation cost
            if (d == 1 and new_d == 2) or (d == 2 and new_d == 1) or \
               (d == 3 and new_d == 4) or (d == 4 and new_d == 3):
                turn_cost = 2
            else:
                turn_cost = 1
            visited.add((r, c, new_d))
            q.append((r, c, new_d, steps + turn_cost))

if __name__ == '__main__':
    main()

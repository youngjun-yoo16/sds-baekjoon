import sys
import collections
import itertools

def main():
    N, M = map(int, sys.stdin.readline().split(" "))
    grid = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    # Precompute all empty cells to avoid TLE
    empty = [(r, c) for r in range(N) for c in range(M) if grid[r][c] == 0]
    # Track the maximum number of safe (0) cells
    max_safe_area = 0

    def bfs():
        nonlocal max_safe_area
        q = collections.deque([])
        # To leave the original grid untouched from future modifications
        # Copy the grid quickly using list comprehension instead of using deepcopy
        grid_copy = [row[:] for row in grid]

        # Enqueue all virus positions
        for r in range(N):
            for c in range(M):
                if grid_copy[r][c] == 2:
                    q.append((r, c))
        
        # BFS to spread the virus to adjacent empty cells
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = dr + row, dc + col
                if 0 <= r < N and 0 <= c < M and grid_copy[r][c] == 0:
                    grid_copy[r][c] = 2
                    q.append((r, c))
        
        # Count remaining safe (0) cells after virus spread
        area = 0
        for row in grid_copy:
            for col in row:
                area += 1 if col == 0 else 0
        
        max_safe_area = max(max_safe_area, area)

    # Try all combinations of placing 3 walls in empty cells
    for walls in itertools.combinations(empty, 3):
        # Place the walls
        for r, c in walls:
            grid[r][c] = 1
        # BFS to spread the virus
        bfs()
        # Unmark the walls for the next combination
        for r, c in walls:
            grid[r][c] = 0
    
    print(max_safe_area)

if __name__=="__main__":
    main()
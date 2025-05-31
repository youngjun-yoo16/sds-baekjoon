from collections import deque

def main():
    n, Q = map(int, input().strip().split(" "))
    N = 2 ** n
    grid = [list(map(int, input().strip().split(" "))) for _ in range(N)]
    L = list(map(int, input().strip().split(" ")))
    visited = set()

    def rotate_and_melt_ice(n):
        nonlocal grid   
        # Size of each subgrid to rotate
        l = 2 ** n
        temp = [[0 for _ in range(N)] for _ in range(N)]

        # Rotate each subgrid 90 degrees clockwise
        for i in range(0, N, l):
            for j in range(0, N, l):
                for r in range(l):
                    for c in range(l):
                        temp[i + r][j + c] = grid[i + (l - c - 1)][j + r]

        grid = [row[:] for row in temp]

        # Melt ice: if a cell has less than 3 ice neighbors, decrease its ice
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    num_ice = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
                            num_ice += 1
                    # Mark for melting
                    if num_ice < 3:
                        temp[r][c] -= 1
        
        # Apply melting changes
        grid = [row[:] for row in temp]
    
    # BFS to find the size of the largest connected ice cluster
    def find_largest_cube(r, c):
        size = 1
        q = deque([(r, c)])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] and (nr, nc) not in visited:
                    size += 1
                    q.append((nr, nc))
                    visited.add((nr, nc))
        return size

    # Apply Q Firestorm spells
    for i in range(Q):
        rotate_and_melt_ice(L[i])
    
    # Find largest block of connected ice
    largest_cube = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] and (r, c) not in visited:
                visited.add((r, c))
                largest_cube = max(largest_cube, find_largest_cube(r, c))

    print(sum(grid[r][c] for r in range(N) for c in range(N)))
    print(largest_cube)

if __name__=="__main__":
    main()
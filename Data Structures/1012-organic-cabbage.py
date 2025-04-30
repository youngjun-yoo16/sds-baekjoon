import sys
import collections

# BFS to explore all connected cabbages
def BFS(grid, q, k, visited):
    M, N = len(grid), len(grid[0])

    while q and k > 0:
        row, col = q.popleft()
        k -= 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < M and 0 <= c < N and grid[r][c] and (r, c) not in visited:
                grid[r][c] = 0
                q.append((r, c))
                visited.add((r, c))

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        worm = 0
        visited = set()
        q = collections.deque()
        cabbage_locations = []
        M, N, K = map(int, sys.stdin.readline().split(" "))
        
        # initialize the grid: M columns x N rows
        grid = [[0 for _ in range(N)] for _ in range(M)]
        
        # read and store cabbage locations
        for _ in range(K):
            cabbage_locations.append(list(map(int, sys.stdin.readline().split(" "))))

        # mark the positions of cabbages on the grid
        for r, c in cabbage_locations:
            grid[r][c] = 1
        
        # iterate through the grid to find clusters of cabbages
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    q.append((r, c))
                    BFS(grid, q, K, visited)
                    worm += 1
        
        print(worm)

if __name__=="__main__":
    main()
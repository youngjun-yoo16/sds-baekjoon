import sys
sys.setrecursionlimit(10 ** 9)

def main():
    N, M = map(int, sys.stdin.readline().split(" "))
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    # Set to track visited characters
    visited = set()
    res = 0

    # DFS to explore unique characters
    def dfs(x, y, num_tiles):
        nonlocal res
        
        if x < 0 or x >= N or y < 0 or y >= M or grid[x][y] in visited:
            return
        
        res = max(res, num_tiles)
        visited.add(grid[x][y])

        dfs(x - 1, y, num_tiles + 1)
        dfs(x + 1, y, num_tiles + 1)
        dfs(x, y - 1, num_tiles + 1)
        dfs(x, y + 1, num_tiles + 1)

        # Backtrack: unmark the character after exploring all paths from it
        visited.remove(grid[x][y])
    
    dfs(0, 0, 1)
    print(res)

if __name__=="__main__":
    main()
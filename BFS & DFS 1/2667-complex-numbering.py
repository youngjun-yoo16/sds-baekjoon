import sys
sys.setrecursionlimit(10 ** 9)

def main():
    N = int(sys.stdin.readline().strip())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    complex_number = 0
    num_houses = []

    # DFS to explore connected houses
    def dfs(x, y):
        nonlocal house_num
        if x < 0 or x >= N or y < 0 or y >= N or not grid[x][y]:
            return

        # Mark this house as visited
        grid[x][y] = 0
        # Count this house
        house_num += 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        
    # Iterate through the whole grid
    for row in range(N):
        for col in range(N):
            if grid[row][col]:
                house_num = 0
                dfs(row, col)
                complex_number += 1
                num_houses.append(house_num)

    print(complex_number)
    
    for count in sorted(num_houses):
        print(count)

if __name__=="__main__":
    main()
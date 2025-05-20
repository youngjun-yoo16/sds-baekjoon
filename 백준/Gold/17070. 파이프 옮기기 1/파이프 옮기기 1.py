import sys

def main():
    N = int(sys.stdin.readline().strip())
    board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    
    # Initialize 3D DP array:
    # dp[0][r][c]: number of ways to reach (r, c) with a horizontal pipe
    # dp[1][r][c]: number of ways to reach (r, c) with a vertical pipe
    # dp[2][r][c]: number of ways to reach (r, c) with a diagonal pipe
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
    
    # Start with the pipe lying horizontally between (0,0) and (0,1)
    dp[0][0][1] = 1
    # Fill the first row where only horizontal movements are possible
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]
    
    # Process the rest of the grid
    for r in range(1, N):
        for c in range(1, N):
            # For horizontal and vertical pipes
            if board[r][c] == 0:
                # Horizontal: from left cell if it's horizontal or diagonal
                dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
                # Vertical: from above cell if it's vertical or diagonal
                dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]
            # Diagonal: from upper-left cell if all three related cells are empty
            if board[r][c] == 0 and board[r - 1][c] == 0 and board[r][c - 1] == 0:
                dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
    
    # Sum all ways to end at (N-1, N-1) regardless of orientation
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))

if __name__=="__main__":
    main()
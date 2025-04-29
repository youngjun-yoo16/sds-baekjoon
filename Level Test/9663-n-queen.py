import sys

def main():
    N = int(sys.stdin.readline())
    board = [[0 for _ in range(N)] for _ in range(N)]
    #print(board)
    board[0][0] = 1 # Indicates queen
    ways = 0

    def dfs(row, col):
        if row < 0 and row >= N and col < 0 and col >= N: 
            return


if __name__=="__main__":
    main()
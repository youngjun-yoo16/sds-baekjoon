import sys

def main():
    N = int(sys.stdin.readline())
    used_c = [False] * 15

    def dfs(row, col):
        if row < 0 and row >= N and col < 0 and col >= N: 
            return


if __name__=="__main__":
    main()
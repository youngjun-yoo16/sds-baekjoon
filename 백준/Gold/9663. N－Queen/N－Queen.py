import sys

def main():
    N = int(sys.stdin.readline())
    grid = [[0] * N for _ in range(N)]
    col = [0] * N
    left_diagonal = [0] * (N * 2)
    right_diagonal = [0] * (N * 2)
    res = 0        

    def backtrack(r):
        nonlocal res

        if r == N:
            res += 1
            return

        for c in range(N):
            if col[c] or left_diagonal[r - c + N] or right_diagonal[r + c]: continue
            
            col[c] = 1
            right_diagonal[r + c] = 1
            left_diagonal[r - c + N] = 1
            grid[r][c] = 1

            backtrack(r + 1)
            
            col[c] = 0
            right_diagonal[r + c] = 0
            left_diagonal[r - c + N] = 0
            grid[r][c] = 0
    
    backtrack(0)
    print(res)

if __name__=="__main__":
    main()
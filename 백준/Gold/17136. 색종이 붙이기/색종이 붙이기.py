import sys

def main():
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]

    # Count of papers used for sizes 1×1 through 5×5
    paper_count = [0] * 6
    best = float('inf')

    def can_place(r, c, size):
        # Check bounds
        if r + size > 10 or c + size > 10:
            return False
        # Ensure all cells in the size×size block are 1
        for i in range(r, r + size):
            for j in range(c, c + size):
                if board[i][j] != 1:
                    return False
        return True

    def place(r, c, size, val):
        # Fill or clear the size×size block
        for i in range(r, r + size):
            for j in range(c, c + size):
                board[i][j] = val

    def backtrack(r, c, used):
        nonlocal best
        # Prune if we've already used too many papers
        if used >= best:
            return

        # Find next cell with a 1
        while r < 10 and board[r][c] == 0:
            c += 1
            if c == 10:
                r += 1
                c = 0

        # If we've covered all rows, update best
        if r == 10:
            best = used
            return

        # Try placing papers from size 5 down to 1
        for size in range(5, 0, -1):
            if paper_count[size] < 5 and can_place(r, c, size):
                paper_count[size] += 1
                place(r, c, size, 0)
                backtrack(r, c, used + 1)
                place(r, c, size, 1)
                paper_count[size] -= 1

    backtrack(0, 0, 0)
    print(-1 if best == float('inf') else best)

if __name__ == "__main__":
    main()
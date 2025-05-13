import sys
import copy
from itertools import permutations

def rotate(p, A):
    r, c, s = p
    for layer in range(1, s+1):
        top, left = r-layer, c-layer
        bottom, right = r+layer, c+layer

        # save the top-left
        tmp = A[top][left]

        for i in range(top, bottom):
            A[i][left] = A[i+1][left]

        for j in range(left, right):
            A[bottom][j] = A[bottom][j+1]

        for i in range(bottom, top, -1):
            A[i][right] = A[i-1][right]

        for j in range(right, left, -1):
            A[top][j] = A[top][j-1]

        A[top][left+1] = tmp

def main():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    rcs = [ [r - 1, c - 1, s] for r, c, s in [map(int, input().split()) for _ in range(k)] ]

    maxVal = int(1e9)

    # Try all permutations of the rotation order
    for p in permutations(rcs):
        g = copy.deepcopy(board)

        for op in p:
            rotate(op, g)

        min_row_sum = min(sum(row) for row in g)
        maxVal = min(maxVal, min_row_sum)

    print(maxVal)

if __name__ == "__main__":
    main()
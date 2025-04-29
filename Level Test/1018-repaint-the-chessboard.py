import sys

# to compute the minimum recoloring cost starting from (start_row, start_col)
def get_min_cost(start_row, start_col, board):
    white_board = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

    black_board = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

    white_recolor, black_recolor = 0, 0
    row = 0

    for i in range(start_row, start_row + 8):
        col = 0
        for j in range(start_col, start_col + 8):
            if board[i][j] != white_board[row][col]:
                white_recolor += 1
            if board[i][j] != black_board[row][col]:
                black_recolor += 1
            col += 1
        row += 1

    return min(white_recolor, black_recolor)

def main():
    N, M = map(int, sys.stdin.readline().split(" "))
    board = []
    for _ in range(N):
        line = sys.stdin.readline().strip()
        board.append(list(line))

    min_cost = float('inf')

    # try every possible 8x8 sub-board
    for i in range(N - 7):
        for j in range(M - 7):
            min_cost = min(min_cost, get_min_cost(i, j, board))

    print(min_cost)

if __name__=="__main__":
    main()
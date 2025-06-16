from collections import deque

def main():
    board = [list(map(int, input().strip())) for _ in range(9)]
    col = [[0] * 10 for _ in range(9)]
    row = [[0] * 10 for _ in range(9)]
    square = [[[0] * 10 for _ in range(3)] for _ in range(3)]

    # 빈칸 리스트 만들기, 사용 중인 수는 사용 처리
    positions = deque()
    for r in range(9):
        for c in range(9):
            if not board[r][c]:
                positions.append((r, c))
            else:
                square[r // 3][c // 3][board[r][c]] = col[c][board[r][c]] = row[r][board[r][c]] = 1

    def backtrack(no_list, idx):
        if idx == len(no_list):
            return True

        r, c = no_list[idx]
        for no in range(1, 10):
            # no가 행, 열, 사각형에서 사용 중이면 패스: 가지 치기
            if row[r][no] or col[c][no] or square[r // 3][c // 3][no]:
                continue

            board[r][c] = no
            square[r // 3][c // 3][no] = col[c][no] = row[r][no] = 1

            if backtrack(no_list, idx + 1):
                return True

            board[r][c] = 0
            square[r // 3][c // 3][no] = col[c][no] = row[r][no] = 0

        return False

    backtrack(positions, 0)
    print('\n'.join(["".join(map(str, b)) for b in board]))
    
if __name__ == '__main__':
    main()
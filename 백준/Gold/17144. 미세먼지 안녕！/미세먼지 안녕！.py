from collections import deque

def main():
    R, C, T = map(int, input().strip().split(" "))
    A = [list(map(int, input().strip().split(" "))) for _ in range (R)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    air_purifier = deque([])
    q = deque([])

    # Find initial positions of dust and the air purifier
    def add_positions():
        for r in range(R):
            for c in range(C):
                if A[r][c] > 0:
                    q.append((r, c))
                if A[r][c] == -1 and len(air_purifier) < 2:
                    air_purifier.append((r, c))
    
    # Step 1: Spread dust particles in all directions
    def spread():
        nonlocal A
        temp = [[0 for _ in range(C)] for _ in range (R)]
        temp[air_purifier_up_pos][0] = temp[air_purifier_down_pos][0] = -1

        while q:
            x, y = q.popleft()
            temp[x][y] += A[x][y]
            amount_spreaded = A[x][y] // 5
            num_directions_spreaded = 0
            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                # Valid and not an air purifier
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in air_purifier:
                    temp[nr][nc] += amount_spreaded
                    num_directions_spreaded += 1
            temp[x][y] -= amount_spreaded * num_directions_spreaded

        A = [row[:] for row in temp]
    
    # Step 2: Operate the air purifier
    def clean(up, down):
        # Upper purifier (counter-clockwise)
        # Up - down
        for r in range(up - 1, 0, -1):
            A[r - 1][0], A[r][0] = A[r][0], A[r - 1][0]
        # Fine dust that was to be cleaned
        A[0][0] = 0
        
        # Up - Left
        for c in range(0, C - 1):
            A[0][c], A[0][c + 1] = A[0][c + 1], A[0][c]
        
        # Up - Up
        for r in range(0, up):
            A[r][C - 1], A[r + 1][C - 1] = A[r + 1][C - 1], A[r][C - 1]
        
        # Up - Right
        for c in range(C - 1, 1, -1):
            A[up][c], A[up][c - 1] = A[up][c - 1], A[up][c]
        
        # Down - Up
        for r in range(down + 1, R - 1):
            A[r + 1][0], A[r][0] = A[r][0], A[r + 1][0]
        # Fine dust that was to be cleaned
        A[R - 1][0] = 0

        # Lower purifier (clockwise)
        # Down - Left
        for c in range(0, C - 1):
            A[R - 1][c], A[R - 1][c + 1] = A[R - 1][c + 1], A[R - 1][c] 

        # Down - Down
        for r in range(R - 1, down, -1):
            A[r][C - 1], A[r - 1][C - 1] = A[r - 1][C - 1], A[r][C - 1]

        # Down - Right
        for c in range(C - 1, 1, -1):
            A[down][c], A[down][c - 1] = A[down][c - 1], A[down][c]

    add_positions()
    air_purifier_up_pos = air_purifier[0][0]
    air_purifier_down_pos = air_purifier[1][0]

    for _ in range(T):
        spread()
        clean(air_purifier_up_pos, air_purifier_down_pos)
        add_positions()

    print(sum(A[r][c] for r in range(R) for c in range(C) if A[r][c] > 0))

if __name__=="__main__":
    main()
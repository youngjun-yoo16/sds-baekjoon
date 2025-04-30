import sys
import collections

def main():
    N, M = map(int, sys.stdin.readline().split(" "))
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    # initialize BFS queue with starting point (row, col, moves)
    q = collections.deque([(0, 0, 1)])
    # set to track visited positions (start from (0, 0))
    visited = set((0, 0))

    while q:
        row, col, moves = q.popleft()

        # reached the bottom-right corner
        if row == N - 1 and col == M - 1:
            print(moves)
            break
            
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            # check bounds and whether cell is unvisited and passable (1 in grid[r][c])
            if 0 <= r < N and 0 <= c < M and grid[r][c] and (r, c) not in visited:
                q.append((r, c, moves + 1))
                visited.add((r, c))

if __name__=="__main__":
    main()
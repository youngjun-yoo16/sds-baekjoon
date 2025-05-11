import sys
import collections

def main():
    N = int(sys.stdin.readline().strip())
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split(" "))
    q = collections.deque([(r1, c1, 0)])
    visited = set((r1, c1))

    # BFS
    while q:
        r, c, moves = q.popleft()

        # Target position reached
        if (r, c) == (r2, c2):
            print(moves)
            return
        
        directions = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
        for dr, dc in directions:
            x, y = dr + r, dc + c
            if 0 <= x < N and 0 <= y < N and (x, y) not in visited:
                q.append((x, y, moves + 1))
                visited.add((x, y))
    
    # Unreachable destination
    print(-1)

if  __name__=="__main__":
    main()
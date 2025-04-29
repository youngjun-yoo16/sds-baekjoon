import sys
import collections

def main():
    N, K = map(int, sys.stdin.readline().split(" "))
    # start from 0 moves, position N, and path list starting from N
    q = collections.deque([(0, N, [N])])
    # to keep track of visited positions to prevent revisiting
    visited = set([N])
    res = 0
    
    # BFS
    while q:
        moves, position, path = q.popleft()
        # print("Moves: " + str(moves) + " Position: " + str(position))

        # reached the target position K
        if position == K:
            print(moves)
            print(*path)
            break
    
        # try all possible moves
        # case 1: move to position + 1
        if 0 <= position + 1 <= 100000 and position + 1 not in visited:
            # mark position as visited as we enqueue it to prevent TLE
            visited.add(position + 1)
            q.append((moves + 1, position + 1, path + [position + 1]))
        # case 2: move to position - 1
        if 0 <= position - 1 <= 100000 and position - 1 not in visited:
            visited.add(position - 1)
            q.append((moves + 1, position - 1, path + [position - 1]))
        # case 3: move to position * 2
        if 0 <= position * 2 <= 100000 and position * 2 not in visited:
            visited.add(position * 2)
            q.append((moves + 1, position * 2, path + [position * 2]))
            
if __name__=="__main__":
    main()
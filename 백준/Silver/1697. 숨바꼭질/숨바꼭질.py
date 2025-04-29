import sys
import collections

def main():
    N, K = map(int, sys.stdin.readline().split(" "))
    # start from 0 moves and position N
    q = collections.deque([(0, N)])
    # to keep track of visited positions to prevent revisiting
    visited = set()
    res = 0

    # BFS
    while q:
        moves, position = q.popleft()
        # print("Moves: " + str(moves) + " Position: " + str(position))

        # reached the target position K
        if position == K:
            res = moves
            break
    
        if position in visited:
            continue
        else:
            # mark current position as visisted
            visited.add(position)
            # try all possible moves
            # case 1: move to position + 1
            if position + 1 >= 0 and position + 1 <= 100000:
                q.append((moves + 1, position + 1))
            # case 2: move to position - 1
            if position - 1 >= 0 and position - 1 <= 100000:
                q.append((moves + 1, position - 1))
            # case 3: move to position * 2
            if position * 2 >= 0 and position * 2 <= 100000:
                q.append((moves + 1, position * 2))
    
    print(res)
            
if __name__=="__main__":
    main()
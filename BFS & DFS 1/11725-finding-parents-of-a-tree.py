import sys
import collections

def main():
    N = int(sys.stdin.readline().strip())
    # Adjacency list to store the tree
    nodeMap = collections.defaultdict(list)
    # Array to store the parent of each node
    parents = [0] * (N + 1)
    # Initialize BFS queue with root node
    q = collections.deque([1])

    for _ in range(N - 1):
        x, y = map(int, sys.stdin.readline().split(" "))
        nodeMap[x].append(y)
        nodeMap[y].append(x)
    
    # BFS
    while q:
        node = q.popleft()
        for children in nodeMap[node]:
            # To prevent revisiting the parent node
            if children != parents[node]:
                # Assign parent
                parents[children] = node
                q.append(children)
    
    for i in range(2, N + 1):
        print(parents[i])

if __name__=="__main__":
    main()
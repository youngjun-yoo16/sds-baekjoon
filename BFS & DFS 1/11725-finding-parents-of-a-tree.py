import sys
import collections

def main():
    N = int(sys.stdin.readline().strip())
    nodeMap = collections.defaultdict(list)
    
    for _ in range(N - 1):
        x, y = map(int, sys.stdin.readline().split(" "))
        
            
    
    print(nodeMap)

if __name__=="__main__":
    main()
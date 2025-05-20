import sys

def main():
    N, M, D = map(int, sys.stdin.readline().split(" "))
    grid = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

if __name__=="__main__":
    main()
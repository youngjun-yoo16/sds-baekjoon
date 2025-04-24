import itertools
import sys

def main():
    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    # genereate only the start team to avoid MLE
    start = list(itertools.combinations(list(range(1, N + 1)), N // 2))    
    min_diff = float('inf')
    for s in start:
        # generate the link team based on the each start team
        link = [p for p in list(range(1, N + 1)) if p not in s]
        start_ability, link_ability = 0, 0
        for p in itertools.permutations(s, 2):
            # subtract 1 bc board is 1-based index
            start_ability += board[p[0] - 1][p[1] - 1]
        for p in itertools.permutations(link, 2):
            link_ability += board[p[0] - 1][p[1] - 1]
        min_diff = min(min_diff, abs(start_ability - link_ability))
    print(min_diff)
    
if __name__ == "__main__":
    main()

from itertools import combinations

def main():
    N, L, R, X = map(int, input().split())
    A = list(map(int, input().split()))

    count = 0
    for i in range(2, N + 1):
        for comb in combinations(A, i):
            if L <= sum(comb) <= R and abs(max(comb) - min(comb)) >= X:
                count += 1

    print(count)

if __name__ == '__main__':
    main()
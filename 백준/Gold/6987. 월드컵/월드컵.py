from itertools import combinations

def main():
    games = list(combinations(range(6), 2))
    res = []

    def backtrack(countries, idx):
        nonlocal valid

        if idx == len(games):
            if all(sum(c) == 0 for c in countries):
                valid = True
            return

        home, away = games[idx]
        # index 0 - win, index 1 - draw, index 2 - lose
        for i in range(3):
            # Case 1: Home win - away lose
            # Case 2: Home draw - away draw
            # Case 3: Home lose - away win
            if countries[home][i] and countries[away][2 - i]:
                countries[home][i] -= 1
                countries[away][2 - i] -= 1

                backtrack(countries, idx + 1)

                countries[home][i] += 1
                countries[away][2 - i] += 1

    for _ in range(4):
        nations = [[] for _ in range(6)]
        decisions = list(map(int, input().split()))
        for i, decision in enumerate(decisions):
            nations[i // 3].append(decision)

        valid = False
        backtrack(nations, 0)
        res.append(1 if valid else 0)

    print(*res)

if __name__ == '__main__':
    main()
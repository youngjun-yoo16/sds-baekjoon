def main():
    N = int(input())
    eggs = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    def count_broken_eggs():
        count = 0
        for durability, weight in eggs:
            if durability <= 0:
                count += 1

        return count

    def backtrack(idx):
        nonlocal res

        # Base case
        if idx == len(eggs):
            broken_eggs_num = count_broken_eggs()
            res = max(res, broken_eggs_num)
            return

        # Already broken egg
        if eggs[idx][0] <= 0:
            backtrack(idx + 1)
            return

        # All other eggs are already broken
        if count_broken_eggs() == len(eggs) - 1:
            res = max(res, len(eggs) - 1)
            return

        for i in range(len(eggs)):
            # Cannot hit itself or another broken egg
            if i == idx or eggs[i][0] <= 0: continue

            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]

            backtrack(idx + 1)

            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]

    backtrack(0)
    print(res)

if __name__ == '__main__':
    main()
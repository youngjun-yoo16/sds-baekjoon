from collections import defaultdict
from itertools import permutations

def main():
    N = int(input())
    info = defaultdict(list)
    numbers = [i for i in range(1, 10)]
    for _ in range(N):
        num, strike, ball = map(int, input().split())
        info[num].append(strike)
        info[num].append(ball)

    count = 0
    for perm in permutations(numbers, 3):
        # 123, 456, etc
        possible = True
        for number in info:
            strike = ball = 0
            number_list = list(map(int, str(number)))
            for i in range(3):
                if number_list[i] == perm[i]:
                    strike += 1
                else:
                    if number_list[i] in perm:
                        ball += 1
            if strike != info[number][0] or ball != info[number][1]:
                possible = False
                break

        if possible:
            count += 1

    print(count)

if __name__ == '__main__':
    main()
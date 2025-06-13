from itertools import combinations

def main():
    heights = []
    for _ in range(9):
        heights.append(int(input()))

    for comb in combinations(heights, 7):
        if sum(comb) == 100:
            for i in comb:
                print(i)
            break

if __name__ == '__main__':
    main()
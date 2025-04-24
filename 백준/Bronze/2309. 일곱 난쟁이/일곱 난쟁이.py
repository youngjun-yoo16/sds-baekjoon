import itertools
import sys

def main():
    array = [int(sys.stdin.readline()) for _ in range(9)]
    combinations =  itertools.combinations(array, 7)
    for group in combinations:
        if sum(group) == 100:
            sorted_group = sorted(group)
            for dwarf in sorted_group:
                print(dwarf)
            break

if __name__ == "__main__":
    main()  
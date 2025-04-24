import itertools
import sys

def main():
    array = [int(sys.stdin.readline()) for _ in range(9)]
    # generate all possible combinations of 7 dwarfs
    combinations =  itertools.combinations(array, 7)
    # iterate through each combination
    for group in combinations:
        if sum(group) == 100:
            # sort in the ascending order of their height
            sorted_group = sorted(group)
            for dwarf in sorted_group:
                print(dwarf)
            break

if __name__ == "__main__":
    main()  


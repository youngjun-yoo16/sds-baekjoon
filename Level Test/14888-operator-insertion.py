import sys
import itertools

def main():
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split(" ")))
    num_operators = list(map(int, sys.stdin.readline().split(" ")))

    operators = []
    # build the operators list based on the number of each operator
    for i in range(len(num_operators)):
        if i == 0 and num_operators[i]:
            operators += '+' * num_operators[i]
        if i == 1 and num_operators[i]:
            operators += '-' * num_operators[i]
        if i == 2 and num_operators[i]:
            operators += 'x' * num_operators[i]
        if i == 3 and num_operators[i]:
            operators += '/' * num_operators[i]
    
    max_num, min_num = float('-inf'), float('inf')
    
    # iterate through all possible unique permutations of operators
    for perm in itertools.permutations(operators):
        numbers_cpy = numbers.copy()
        i = 1

        # insert operators between numbers
        for p in perm:
            numbers_cpy.insert(i, p)
            i += 2

        # evaluate the expression left to right
        for i in range(0, len(numbers_cpy) - 2, 2):
            num1 = numbers_cpy[i] if i == 0 else num1
            op = numbers_cpy[i + 1]
            num2 = numbers_cpy[i + 2]

            if op == '+':
                num1 = num1 + num2
            elif op == '-':
                num1 = num1 - num2
            elif op == 'x':
                num1 = num1 * num2
            else:
                if num1 < 0:
                    # special rule for negative integer division
                    num1 = -num1 // num2
                    num1 = -num1
                else:
                    num1 = num1 // num2

        max_num = max(max_num, num1)
        min_num = min(min_num, num1)
    
    print(max_num)
    print(min_num)

if __name__=="__main__":
    main()
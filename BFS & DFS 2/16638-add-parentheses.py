import sys
sys.setrecursionlimit(10**7)

def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:  # op == '*'
        return a * b

def main():
    N = int(sys.stdin.readline().strip())
    expr = sys.stdin.readline().strip()
    
    # Split into numbers and operators
    nums = [int(expr[i]) for i in range(0, N, 2)]
    ops  = [expr[i] for i in range(1, N, 2)]
    M = len(ops)
    
    # Keep track of the maximum result seen
    max_result = -2 ** 31

    def dfs(idx, current):
        nonlocal max_result

        # If we've applied all operators, record the final value
        if idx >= M:
            max_result = max(max_result, current)
            return

        # 1) No parentheses on ops[idx]: just do it
        v1 = calc(current, nums[idx + 1], ops[idx])
        dfs(idx + 1, v1)

        # 2) If possible, put parentheses around the next operator (ops[idx+1])
        #    i.e. compute (nums[idx+1] ops[idx+1] nums[idx+2]) first,
        #    then apply ops[idx] between current and that bracket.
        if idx + 1 < M:
            bracket = calc(nums[idx + 1], nums[idx + 2], ops[idx + 1])
            v2 = calc(current, bracket, ops[idx])
            dfs(idx + 2, v2)

    dfs(0, nums[0])

    print(max_result)

if __name__ == "__main__":
    main()
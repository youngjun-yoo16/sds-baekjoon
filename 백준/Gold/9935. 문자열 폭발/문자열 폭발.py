import sys

def main():
    string = list(sys.stdin.readline().strip())
    explosion_string = list(sys.stdin.readline().strip())
    stack = []

    for s in string:
        stack.append(s)
        # if the last character matches and stack ends with the explosion string
        if s == explosion_string[-1] and stack[-len(explosion_string):] == explosion_string:
            # pop the explosion string from the stack
            for _ in range(len(explosion_string)):
                stack.pop()
    
    print(''.join(stack)) if stack else print("FRULA")

if __name__=="__main__":
    main()
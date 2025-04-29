import sys

def main():
    T = int(sys.stdin.readline())
    data = []
    for _ in range(T):
        ps = list(sys.stdin.readline().strip())
        data.append(ps)
    
    for ps in data:
        flag = False
        stack = []
        for p in ps:
            if p == "(":
                stack.append(p)
            else:
                if stack:
                    stack.pop()
                else:
                    print("NO")
                    flag = True
                    break
        
        if not flag:
            if stack:
                print("NO")
            else:
                print("YES")

if __name__=="__main__":
    main()
def main():
    arr = list(map(int, input().split()))
    choices = []
    cnt = 0

    def dfs(level):
        nonlocal cnt

        if level == 10:
            score = 0
            for i in range(10):
                if arr[i] == choices[i]:
                    score += 1
                if i >= 2:
                    if choices[i] == choices[i - 1] == choices[i - 2]:
                        return
            if score >= 5:
                cnt += 1
            return

        for i in range(1, 6):
            choices.append(i)
            dfs(level + 1)
            choices.pop()

    dfs(0)
    print(cnt)

if __name__ == '__main__':
    main()
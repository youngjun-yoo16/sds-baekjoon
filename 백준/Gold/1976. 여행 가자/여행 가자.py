def main():
    N = int(input())
    M = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    plan = list(map(int, input().split()))
    parents = [i for i in range(N + 1)]

    def find_set(a):
        if parents[a] == a:
            return a
        parents[a] = find_set(parents[a])
        return find_set(parents[a])

    def union(a, b):
        a_root = find_set(a)
        b_root = find_set(b)

        if a_root == b_root:
            return

        parents[b_root] = a_root

    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                union(r + 1, c + 1)

    flag = find_set(plan[0])
    for p in plan[1:]:
        if find_set(parents[p]) != flag:
            print("NO")
            return

    print("YES")

if __name__ == '__main__':
    main()
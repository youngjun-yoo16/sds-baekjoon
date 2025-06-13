from collections import defaultdict

def main():
    N = int(input())
    M = int(input())
    adj_list = defaultdict(list)
    for _ in range(M):
        i, j = map(int, input().split())
        adj_list[i].append(j)
        adj_list[j].append(i)

    def dfs(v, visit):
        if v in visit:
            return

        visit.add(v)

        for u in adj_list[v]:
            dfs(u, visit)

    visited = set()
    dfs(1, visited)

    print(len(visited) - 1)

if __name__ == '__main__':
    main()
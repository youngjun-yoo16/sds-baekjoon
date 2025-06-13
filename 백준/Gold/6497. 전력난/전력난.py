import sys
sys.setrecursionlimit(10**6)

def main():
    res = []
    while True:
        m, n = map(int, sys.stdin.readline().split())

        if not m and not n:
            break

        edge_list =  [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        edge_list.sort(key=lambda x: x[2])
        parents = [i for i in range(n)]

        def find_set(a):
            if parents[a] == a:
                return a
            parents[a] = find_set(parents[a])
            return find_set(parents[a])

        def union(a, b):
            root_a = find_set(a)
            root_b = find_set(b)
            if root_a != root_b:
                parents[root_a] = root_b
                return True
            return False

        count = total_cost = 0

        for from_a, to_a, cost in edge_list:
            if union(from_a, to_a):
                total_cost += cost
                count += 1
                if count == m - 1:
                    break

        res.append(sum(edge_list[i][2] for i in range(n)) - total_cost)

    for r in res:
        print(r)

if __name__ == '__main__':
    main()
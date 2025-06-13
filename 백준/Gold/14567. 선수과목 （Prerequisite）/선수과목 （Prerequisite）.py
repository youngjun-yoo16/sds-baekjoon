from collections import defaultdict, deque

def main():
    N, M = map(int, input().split())
    adj_list = defaultdict(list)
    indegree = [0] * (N + 1)
    semester = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        indegree[b] += 1

    q = deque()
    count = 1
    for i in range(1, N + 1):
        if not indegree[i]:
            q.append(i)
            semester[i] = count

    count += 1
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            for v in adj_list[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    if not semester[v]:
                        semester[v] = count
        count += 1

    for i in range(1, N + 1):
        if semester[i]:
            print(semester[i], end=' ')

if __name__ == '__main__':
    main()
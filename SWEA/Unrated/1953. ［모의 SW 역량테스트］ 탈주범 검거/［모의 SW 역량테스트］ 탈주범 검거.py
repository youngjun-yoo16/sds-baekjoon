from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    def possible_architectures(cur_arch, d):
        '''
        1. 상 하 좌 우
        2. 상 하
        3. 좌 우
        4, 상 우
        5. 하 우
        6. 하 좌
        7. 상 좌
        '''  
        arch_map = {(-1, 0) : {1, 2, 5, 6}, (1, 0) : {1, 2, 4, 7},
                    (0, -1) : {1, 3, 4, 5}, (0, 1) : {1, 3, 6, 7}}

        possible_dirs = {1 : {(-1, 0), (1, 0), (0, 1), (0, -1)},
                         2 : {(-1, 0), (1, 0)},
                         3 : {(0, -1), (0, 1)},
                         4 : {(-1, 0), (0, 1)},
                         5 : {(1, 0), (0, 1)},
                         6 : {(0, -1), (1, 0)},
                         7 : {(0, -1), (-1, 0)}}

        if d in possible_dirs[cur_arch]:
            return arch_map[d]
        
        return {}
    
    res = []
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    q = deque([(R, C)])
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True

    for _ in range(L - 1):
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and tunnel[nr][nc] and not visited[nr][nc]:
                    can_go = possible_architectures(tunnel[r][c], (dr, dc))
                    if can_go and tunnel[nr][nc] in can_go:
                        visited[nr][nc] = True
                        q.append((nr, nc))

    count = (sum(sum(row) for row in visited))
    print(f"#{test_case} {count}")

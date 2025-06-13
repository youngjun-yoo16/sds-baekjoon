from collections import deque

def main():
    N, M, A, B, K = map(int, input().split())
    grid = [[0 for _ in range(M)] for _ in range(N)]
    blockers = deque()

    for _ in range(K):
        r, c = map(int, input().split())
        grid[r - 1][c - 1] = -1
        blockers.append((r - 1, c - 1))

    start_r, start_c = map(int, input().split())
    start_up_left_r, start_up_left_c = start_r - 1, start_c - 1

    dest_r, dest_c = map(int, input().split())
    dest_r, dest_c = dest_r - 1, dest_c - 1

    q = deque([(start_up_left_r, start_up_left_c, 0)])
    visited = {(start_up_left_r, start_up_left_c)}
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        r, c, step = q.popleft()

        if (r, c) == (dest_r, dest_c):
            print(step)
            return

        for dr, dc in direction:
            ulr, ulc = r + dr, c + dc
            urr, urc = ulr, ulc + B -1
            dlr, dlc = ulr + A - 1, ulc

            if 0 <= ulr < N and 0 <= ulc < M and 0 <= urc < M and 0 <= dlr < N and (ulr, ulc) not in visited:
                # 유닛이 한칸 이동할때 장애물과 겹치는 부분이 하나라도 생기면 바로 break
                broke = False
                for x in range(ulr, dlr + 1):
                    for y in range(ulc, urc + 1):
                        if grid[x][y] == -1:
                            broke = True
                            break
                # 유닛이 이동했을때 모든 장애물과 겹치지 않음
                if not broke:
                    q.append((ulr, ulc, step + 1))
                    visited.add((ulr, ulc))

    print(-1)

if __name__ == '__main__':
    main()
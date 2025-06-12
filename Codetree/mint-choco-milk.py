import heapq
from collections import deque

def main():
    N, T = map(int, input().split(' '))
    F = list(list(set(i) for i in input().strip()) for _ in range(N))
    B = list(list(map(int, input().split(' '))) for _ in range(N))

    def form_group_find_leader(x, y, visited):
        original_food = F[x][y]
        q = deque([(x, y)])
        group = set([(x, y)])
        belief = [(-B[x][y], x, y)]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and F[nr][nc] == original_food and (nr, nc) not in visited:
                    group.add((nr, nc))
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    heapq.heappush(belief, (-B[nr][nc], nr, nc))

        leader = heapq.heappop(belief)
        return group, leader[1], leader[2]

    def spread(score, r, c, spreaded):
        eagerness = -score - 1
        B[r][c] = 1

        spread_dir = -score % 4

        # Up
        if spread_dir == 0:
            direction = (-1, 0)
            nr, nc = r + direction[0], c + direction[1]
            while 0 <= nr < N and 0 <= nc < N and eagerness > 0:
                if F[nr][nc] != F[r][c]:
                    # 강한 전파
                    if eagerness > B[nr][nc]:
                        F[nr][nc] = F[r][c].copy()
                        eagerness -= (B[nr][nc] + 1)
                        B[nr][nc] += 1
                    # 약한 전파
                    else:
                        F[nr][nc].update(F[r][c].copy())
                        B[nr][nc] += eagerness
                        eagerness = 0
                    
                    spreaded.add((nr, nc))

                nr += direction[0]
                nc += direction[1]
        # Down
        elif spread_dir == 1:
            direction = (1, 0)
            nr, nc = r + direction[0], c + direction[1]
            while 0 <= nr < N and 0 <= nc < N and eagerness > 0:
                if F[nr][nc] != F[r][c]:
                    # 강한 전파
                    if eagerness > B[nr][nc]:
                        F[nr][nc] = F[r][c].copy()
                        eagerness -= (B[nr][nc] + 1)
                        B[nr][nc] += 1
                    # 약한 전파
                    else:
                        F[nr][nc].update(F[r][c].copy())
                        B[nr][nc] += eagerness
                        eagerness = 0
                    
                    spreaded.add((nr, nc))

                nr += direction[0]
                nc += direction[1]
        # Left
        elif spread_dir == 2:
            direction = (0, -1)
            nr, nc = r + direction[0], c + direction[1]
            while 0 <= nr < N and 0 <= nc < N and eagerness > 0:
                if F[nr][nc] != F[r][c]:
                    # 강한 전파
                    if eagerness > B[nr][nc]:
                        F[nr][nc] = F[r][c].copy()
                        eagerness -= (B[nr][nc] + 1)
                        B[nr][nc] += 1
                    # 약한 전파
                    else:
                        F[nr][nc].update(F[r][c].copy())
                        B[nr][nc] += eagerness
                        eagerness = 0
                    
                    spreaded.add((nr, nc))

                nr += direction[0]
                nc += direction[1]
        # Right
        else:
            direction = (0, 1)
            nr, nc = r + direction[0], c + direction[1]
            while 0 <= nr < N and 0 <= nc < N and eagerness > 0:
                if F[nr][nc] != F[r][c]:
                    # 강한 전파
                    if eagerness > B[nr][nc]:
                        F[nr][nc] = F[r][c].copy()
                        eagerness -= (B[nr][nc] + 1)
                        B[nr][nc] += 1
                    # 약한 전파
                    else:
                        F[nr][nc].update(F[r][c].copy())
                        B[nr][nc] += eagerness
                        eagerness = 0
                    
                    spreaded.add((nr, nc))

                nr += direction[0]
                nc += direction[1]

    for _ in range(T):
        # 1. Morning
        for r in range(N):
            for c in range(N):
                B[r][c] += 1

        # 2. Lunch
        visited = set([])
        single_food, double_comb, triple_comb = [], [], []
        for r in range(N):
            for c in range(N):
                if (r, c) not in visited:
                    visited.add((r, c))
                    group, leader_r, leader_c = form_group_find_leader(r, c, visited)
                    B[leader_r][leader_c] += len(group) - 1

                    # 단일, 이중, 삼중 구분
                    if len(F[leader_r][leader_c]) == 1:
                        heapq.heappush(single_food, (-B[leader_r][leader_c], leader_r, leader_c))
                    elif len(F[leader_r][leader_c]) == 2:
                        heapq.heappush(double_comb, (-B[leader_r][leader_c], leader_r, leader_c))
                    else:
                        heapq.heappush(triple_comb, (-B[leader_r][leader_c], leader_r, leader_c))
                    
                    for x, y in group:
                        if (x, y) != (leader_r, leader_c):
                            B[x][y] -= 1
    
        # 3. Dinner
        spreaded = set()
        while single_food:
            score, r, c = heapq.heappop(single_food)
            # 전파를 당하지 않았으면 전파 가능
            if (r, c) not in spreaded:
                spread(score, r, c, spreaded)
        while double_comb:
            score, r, c = heapq.heappop(double_comb)
            if (r, c) not in spreaded:
                spread(score, r, c, spreaded)
        while triple_comb:
            score, r, c = heapq.heappop(triple_comb)
            if (r, c) not in spreaded:
                spread(score, r, c, spreaded)
              
        mint_choco_milk = mint_choco = mint_milk = choco_milk = milk = choco = mint = 0

        for r in range(N):
            for c in range(N):
                cur_food = F[r][c]
                cur_score = B[r][c]
                if 'M' in cur_food and 'T' in cur_food and 'C' in cur_food:
                    mint_choco_milk += cur_score
                elif 'T' in cur_food and 'C' in cur_food:
                    mint_choco += cur_score
                elif 'T' in cur_food and 'M' in cur_food:
                    mint_milk += cur_score
                elif 'C' in cur_food and 'M' in cur_food:
                    choco_milk += cur_score
                elif 'M' in cur_food:
                    milk += cur_score
                elif 'C' in cur_food:
                    choco += cur_score
                else:
                    mint += cur_score
            
        print(mint_choco_milk, mint_choco, mint_milk, choco_milk, milk, choco, mint)

if __name__ == '__main__':
    main()
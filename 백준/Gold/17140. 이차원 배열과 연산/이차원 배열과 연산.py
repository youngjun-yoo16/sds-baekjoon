"""
R 연산: 행의 개수 >= 열의 개수
C 연산: 행의 개수 < 열의 개수
처음엔 3x3이므로 R 연산이 무조건 먼저 시행됨
각 행을 루프를 돌리고 힙에 (나온 횟수, 숫자) 로 정렬 하기
정렬 시 0은 무시 하기 ex: [3, 2, 0, 0]은 (2, 1) (3, 1)과 같다.
모든 행 정렬 후 제일 길이가 긴 행 찾기 (len(힙) * 2)
그 행의 길이를 기준 으로 새로운 배열을 만들기
이 모든 것이 1초
각 정렬 마다 (r, c) 값 체크 - k 이면 종료
100초가 지나도 k 가 안 나오면 -1 출력
"""
import heapq
from collections import defaultdict

def main():
    r, c, k = map(int, input().split())
    r -= 1
    c -= 1

    A = [list(map(int, input().split())) for _ in range(3)]

    def R():
        temp = []

        for x in range(len(A)):
            num_count_map = defaultdict(int)
            for y in range(len(A[x])):
                # 0은 제외
                if A[x][y]:
                    num_count_map[A[x][y]] += 1

            lst = []
            for key, val in num_count_map.items():
                lst.append((key, val))

            lst.sort(key=lambda e: (e[1], e[0]))

            res = []
            for item in lst:
                for i in item:
                    res.append(i)
            temp.append(res)

        # Find list with max length
        max_length = len(max(temp, key=len))

        # max_length 길이 보다 작은 행들 뒤에 0 붙여 주기
        for i in range(len(temp)):
            if len(temp[i]) < max_length:
                for c in range(len(temp[i]), max_length):
                    temp[i].append(0)

        return temp

    def C():
        temp = []

        for y in range(len(A[0])):
            num_count_map = defaultdict(int)
            for x in range(len(A)):
                if A[x][y]:
                    num_count_map[A[x][y]] += 1

            lst = []
            for key, val in num_count_map.items():
                lst.append((key, val))

            lst.sort(key=lambda e: (e[1], e[0]))

            res = []
            for item in lst:
                for i in item:
                    res.append(i)
            temp.append(res)

        # Find list with max length
        max_length = 0
        if temp:
            max_length = len(max(temp, key=len))

        # max_length 길이 보다 작은 행들 뒤에 0 붙여 주기
        for i in range(len(temp)):
            if len(temp[i]) < max_length:
                for c in range(len(temp[i]), max_length):
                    temp[i].append(0)

        num_new_rows = max_length
        num_new_cols = len(temp)
        new_A = [[0] * num_new_cols for _ in range(num_new_rows)]

        for r in range(num_new_rows):
            for c in range(num_new_cols):
                new_A[r][c] = temp[c][r]

        return new_A

    time = 0
    while True:
        if 0 <= r < len(A) and 0 <= c < len(A[0]):
            if A[r][c] == k:
                print(time)
                break

        if time >= 100:
            print(-1)
            break

        # R 연산: 행의 개수 >= 열의 개수
        if len(A) >= len(A[0]):
            arr = R()
            A = [row[:] for row in arr]
        # C 연산: 행의 개수 < 열의 개수
        else:
            arr = C()
            A = [row[:] for row in arr]

        if len(A) > 100:
            A = A[:100]

        if len(A[0]) > 100:
            A = [row[:100] for row in A]

        time += 1

if __name__ == '__main__':
    main()
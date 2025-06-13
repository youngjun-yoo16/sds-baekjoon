from collections import deque


def main():
    F, S, G, U, D = map(int, input().split())
    q = deque([S])
    visited = {S}
    directions = [U, -D]
    count = 0

    while q:
        for _ in range(len(q)):
            x = q.popleft()

            if x == G:
                print(count)
                return

            for d in directions:
                nx = x + d
                if 1 <= nx <= F and nx not in visited:
                    q.append(nx)
                    visited.add(nx)

        count += 1

    print("use the stairs")

if __name__ == '__main__':
    main()
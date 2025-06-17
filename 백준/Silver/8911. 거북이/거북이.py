def main():
    T = int(input())

    # East, North, West, South
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(T):
        idx = 1
        x = y = max_x = max_y = min_x = min_y = 0
        commands = list(input())
        for command in commands:
            dy, dx = directions[idx]
            if command == 'F':
                x += dx
                y += dy
            elif command == 'B':
                x += -dx
                y += -dy
            elif command == 'L':
                idx = (idx + 1) % 4
            else:
                idx = (idx + 3) % 4

            max_x, max_y = max(max_x, x), max(max_y, y)
            min_x, min_y = min(min_x, x), min(min_y, y)
     
        print((max_y - min_y) * (max_x - min_x))

if __name__ == '__main__':
    main()
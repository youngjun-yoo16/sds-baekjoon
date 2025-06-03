def main():
    N, M = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(N)]
    spells = [tuple(map(int, input().strip().split())) for _ in range(M)]

    # Direction mappings: up, down, left, right
    dir_map = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

    # Shark is at the center of the grid
    center = (N // 2, N // 2)

    # Score tracking: index 1, 2, 3 for marble types
    score = [0, 0, 0, 0]

    # Generate the spiral order path from the center
    def generate_spiral_positions():
        spiral = []
        r, c = center
        step = 1
        # Left, down, right, up
        direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        while True:
            for d in range(4):
                for _ in range(step):
                    r += direction[d][0]
                    c += direction[d][1]
                    if 0 <= r < N and 0 <= c < N:
                        spiral.append((r, c))
                    else:
                        return spiral
                if d % 2 == 1:
                    step += 1

    spiral_path = generate_spiral_positions()

    # Perform the Blizzard spell
    def cast_blizzard(d, s):
        r, c = center
        dr, dc = dir_map[d]
        for i in range(1, s + 1):
            nr, nc = r + dr * i, c + dc * i
            if 0 <= nr < N and 0 <= nc < N:
                grid[nr][nc] = 0

    # Flatten the grid to a marble list based on spiral path
    def flatten():
        marbles = []
        for r, c in spiral_path:
            if grid[r][c]:
                marbles.append(grid[r][c])
        return marbles

    # Write marbles back into the grid from spiral path
    def expand(marbles):
        for r, c in spiral_path:
            grid[r][c] = 0
        for i in range(min(len(marbles), len(spiral_path))):
            r, c = spiral_path[i]
            grid[r][c] = marbles[i]

    # Explode groups of 4 or more same-type marbles
    def explode(marbles):
        changed = False
        new_marbles = []
        i = 0
        while i < len(marbles):
            j = i
            while j < len(marbles) and marbles[j] == marbles[i]:
                j += 1
            count = j - i
            if count >= 4:
                changed = True
                score[marbles[i]] += count
            else:
                new_marbles.extend(marbles[i:j])
            i = j
        return new_marbles, changed

    # Transform marbles into group counts and values
    def change(marbles):
        new_marbles = []
        i = 0
        while i < len(marbles):
            j = i
            while j < len(marbles) and marbles[j] == marbles[i]:
                j += 1
            count = j - i
            num = marbles[i]
            new_marbles.extend([count, num])
            i = j
        return new_marbles[:len(spiral_path)]

    # Run the M spells in order
    for d, s in spells:
        cast_blizzard(d, s)
        marbles = flatten()
        while True:
            marbles, exploded = explode(marbles)
            if not exploded:
                break
        marbles = change(marbles)
        expand(marbles)

    print(score[1] * 1 + score[2] * 2 + score[3] * 3)

if __name__ == "__main__":
    main()
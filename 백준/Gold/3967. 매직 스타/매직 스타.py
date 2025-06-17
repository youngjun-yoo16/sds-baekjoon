from collections import defaultdict

def main():
    grid = [list(input().strip()) for _ in range(5)]
    alphabet_to_val = { 'A' : 1, 'B' : 2, 'C' : 3,
                        'D' : 4, 'E' : 5, 'F' : 6,
                        'G' : 7, 'H' : 8, 'I' : 9,
                        'J' : 10, 'K' : 11, 'L' : 12 }
    line_to_cells = { 1 : [(0, 4), (1, 3), (2, 2), (3, 1)],
                      2 : [(3, 1), (3, 3), (3, 5), (3, 7)],
                      3 : [(0, 4), (1, 5), (2, 6), (3, 7)],
                      4 : [(1, 1), (1, 3), (1, 5), (1, 7)],
                      5 : [(1, 1), (2, 2), (3, 3), (4, 4)],
                      6 : [(1, 7), (2, 6), (3, 5), (4, 4)] }
    magic_star = { 1 : set(), 2 : set(), 3 : set(), 
                   4 : set(), 5 : set(), 6 : set() }
    used = [False] * 13
    empty = []

    for r in range(5):
        for c in range(9):
            if grid[r][c] == 'x':
                empty.append((r, c))
            elif grid[r][c] != '.':
                for line in line_to_cells:
                    if (r, c) in line_to_cells[line]:
                        val = alphabet_to_val[grid[r][c]]
                        magic_star[line].add(val)
                        used[val] = True

    cell_to_lines = defaultdict(list)
    for line, coord in line_to_cells.items():
        for r, c in coord:
            cell_to_lines[(r, c)].append(line)

    def backtrack(pos, idx):
        if idx == len(pos):
            return True

        r, c = pos[idx]

        for a in alphabet_to_val:
            val = alphabet_to_val[a]
            if used[val]:
                continue

            lines = cell_to_lines[(r, c)]

            # Check all lines this cell affects
            if any(
                len(magic_star[l]) == 4 or
                (len(magic_star[l]) == 3 and sum(magic_star[l]) + val != 26) or
                sum(magic_star[l]) + val > 26
                for l in lines
            ):
                continue

            grid[r][c] = a
            used[val] = True
            for l in lines:
                magic_star[l].add(val)

            if backtrack(pos, idx + 1):
                return True

            grid[r][c] = 'x'
            used[val] = False
            for l in lines:
                magic_star[l].remove(val)

        return False

    backtrack(empty, 0)
    print('\n'.join(["".join(g) for g in grid]))

if __name__ == '__main__':
    main()
def main():
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    PR, PC = map(lambda x: int(x) - 1, input().split())
    
    # East, North, West, South
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    letter_directions = { 0 : "R", 1 : "U", 2 : "L", 3 : "D" }

    def bfs(idx):
        original_dir = letter_directions[idx]
        visited = set()
        r, c = PR, PC
        time = 0

        while 0 <= r < N and 0 <= c < M and grid[r][c] != 'C':

            if not((0 <= r < N) and (0 <= c < M)) or grid[r][c] == 'C':
                break

            if (r, c, idx) in visited:
                return -1, original_dir
            
            visited.add((r, c, idx))

            # In case when light hits mirror at the very first move
            if grid[r][c] == '/':
                # Turn left 90 degrees when coming from either east or west
                if idx == 0 or idx == 2:
                    idx = (idx + 1) % 4
                # Turn right 90 degrees otherwise
                else:
                    idx = (idx + 3) % 4
            
            if grid[r][c] == '\\':
                # Turn left 90 degrees when coming from either north or south
                if idx == 1 or idx == 3:
                    idx = (idx + 1) % 4
                # Turn right 90 degrees otherwise
                else:
                    idx = (idx + 3) % 4
            dr, dc = directions[idx]
            r += dr
            c += dc

            time += 1
        
        return time, original_dir

    u, u_letter = bfs(1)
    r, r_letter = bfs(0)
    d, d_letter = bfs(3)
    l, l_letter = bfs(2)
    
    letter = None

    if u == -1:
        letter = u_letter
    elif r == -1:
        letter = r_letter
    elif d == -1:
        letter = d_letter
    elif l == -1:
        letter = l_letter
    
    if letter != None:
        print(letter)
        print("Voyager")
    else:
        max_time = max(u, r, d, l)

        # Fixed logic to deal with multiple directions resulting in the same maximum time
        if u == max_time:
            print('U')
        elif r == max_time:
            print('R')
        elif d == max_time:
            print('D')
        else:
            print('L')
    
        print(max_time)


if __name__=="__main__":
    main()
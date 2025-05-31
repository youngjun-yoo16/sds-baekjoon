from collections import deque

def main():
    N, M, K = map(int, input().strip().split(" "))
    grid = [list(map(int, input().strip().split(" "))) for _ in range(N)]
    dice = { "up" : 1, "right" : 3, "left" : 4, "front" : 2, "back" : 5, "down" : 6}
    
    # Rotate direction based on clockwise flag and current direction
    def rotate_dice(clockwise, dir):
        match dir:
            case "east":
                return "south" if clockwise else "north"
            case "west":
                return "north" if clockwise else "south"
            case "north":
                return "east" if clockwise else "west"
            case "south":
                return "west" if clockwise else "east"

    # Updates the dice values when moved in a given direction        
    def set_dice(dir):
        nonlocal dice
        rotated_dice = {}

        match dir:
            case "east":
                rotated_dice["down"] = dice["right"]
                rotated_dice["right"] = dice["up"]
                rotated_dice["up"] = dice["left"]
                rotated_dice["left"] = dice["down"]
                rotated_dice["front"] = dice["front"]
                rotated_dice["back"] = dice["back"]

            case "west":
                rotated_dice["down"] = dice["left"]
                rotated_dice["right"] = dice["down"]
                rotated_dice["up"] = dice["right"]
                rotated_dice["left"] = dice["up"]
                rotated_dice["front"] = dice["front"]
                rotated_dice["back"] = dice["back"]

            case "south":
                rotated_dice["down"] = dice["back"]
                rotated_dice["right"] = dice["right"]
                rotated_dice["up"] = dice["front"]
                rotated_dice["left"] = dice["left"]
                rotated_dice["front"] = dice["down"]
                rotated_dice["back"] = dice["up"]

            case "north":
                rotated_dice["down"] = dice["front"]
                rotated_dice["right"] = dice["right"]
                rotated_dice["up"] = dice["back"]
                rotated_dice["left"] = dice["left"]
                rotated_dice["front"] = dice["up"]
                rotated_dice["back"] = dice["down"]
        
        dice = rotated_dice.copy()
    
    # BFS to calculate score from connected region with same number
    def bfs(r, c):
        cur_score = grid[r][c]
        q = deque([(r, c)])
        visited = set([(r, c)])
        cells = 1

        while q:
            r, c = q.popleft()
            for dr, dc in zip(dx, dy):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == cur_score and (nr, nc) not in visited:
                    cells += 1
                    q.append((nr, nc))
                    visited.add((nr, nc))
        
        return cur_score * cells

    # Initial direction and starting point
    direction = "east"
    r = c = 0
    res = 0

    # Direction vectors: east, west, north, south
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for _ in range(K):
        # Move based on current direction and bounce if out of bounds
        if direction == "east":
            nr = r + dx[0]
            nc = c + dy[0]
            if 0 <= nr < N and 0 <= nc < M:
                r, c = nr, nc
                set_dice(direction)
            else:
                direction = "west"
                r += dx[1]
                c += dy[1]
                set_dice(direction)
        elif direction == "west":
            nr = r + dx[1]
            nc = c + dy[1]
            if 0 <= nr < N and 0 <= nc < M:
                r, c = nr, nc
                set_dice(direction)
            else:
                direction = "east"
                r += dx[0]
                c += dy[0]
                set_dice(direction)
        elif direction == "north":
            nr = r + dx[2]
            nc = c + dy[2]
            if 0 <= nr < N and 0 <= nc < M:
                r, c = nr, nc
                set_dice(direction)
            else:
                direction = "south"
                r += dx[3]
                c += dy[3]
                set_dice(direction)
        else:
            nr = r + dx[3]
            nc = c + dy[3]
            if 0 <= nr < N and 0 <= nc < M:
                r, c = nr, nc
                set_dice(direction)
            else:
                direction = "north"
                r += dx[2]
                c += dy[2]
                set_dice(direction)
        
        # Calculate score at the new position
        res += bfs(r, c)

        # Determine next direction based on dice bottom (A) and current cell (B)
        # Clockwise if A > B
        if dice["down"] > grid[r][c]:
            direction = rotate_dice(True, direction) 
        # Counter-clockwise if A < B
        elif dice["down"] < grid[r][c]:
            direction = rotate_dice(False, direction)
    
    print(res)

if __name__=="__main__":
    main()
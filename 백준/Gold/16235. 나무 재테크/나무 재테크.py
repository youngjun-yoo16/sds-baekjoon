from collections import deque

def main():
    N, M, K = map(int, input().strip().split(" "))
    # Additional nutrients added to each cell during winter
    food = [list(map(int, input().strip().split(" "))) for _ in range(N)]
    # Initialize the nutrient grid with 5 units of nutrients in each cell
    grid = [[5 for _ in range(N)] for _ in range(N)]
    # Each cell holds a list of tree ages
    trees = [[deque() for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        x, y, z = map(int, input().strip().split(" "))
        trees[x - 1][y - 1].append(z)

    # Initial sort for all deques: youngest to the left
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                sorted_ages = sorted(list(trees[r][c]))
                trees[r][c] = deque(sorted_ages)

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Simulate K years
    for _ in range(K):
        # SPRING: Trees eat nutrients and grow, or die
        dead_nutrients_this_year = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if trees[r][c]:
                    num_trees_in_cell = len(trees[r][c])
                    grown_and_survived_trees = deque() # Temp deque for survivors
                    for _ in range(num_trees_in_cell):
                        # Youngest tree eats first
                        age = trees[r][c].popleft()
                        if grid[r][c] >= age:
                            grid[r][c] -= age
                            # Add to right, maintains sorted order
                            grown_and_survived_trees.append(age + 1)   
                        else:
                            dead_nutrients_this_year[r][c] += age // 2
                    # Update cell with survivors 
                    trees[r][c] = grown_and_survived_trees

        # SUMMER: Add nutrients from dead trees
        for r in range(N):
            for c in range(N):
                grid[r][c] += dead_nutrients_this_year[r][c]
        
        # FALL: Trees reproduce
        # Count how many new saplings each cell receives to optimize deque creation
        num_new_saplings_for_cell = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                for age in trees[r][c]:
                    if age % 5 == 0:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < N and 0 <= nc < N:
                                num_new_saplings_for_cell[nr][nc] += 1
        
        # ADd new saplings to the front of the deques
        for r in range(N):
            for c in range(N):
                if num_new_saplings_for_cell[r][c] > 0:
                    # Create a deque of new saplings  (all age 1)
                    newly_born_saplings = deque([1] * num_new_saplings_for_cell[r][c])
                    # Prepend these new saplings to the existing deque in cell (r,c)
                    newly_born_saplings.extend(trees[r][c])
                    trees[r][c] = newly_born_saplings
                    
        # WINTER: Add nutrients from the food matrix to the soil
        for r in range(N):
            for c in range(N):
                grid[r][c] += food[r][c]
    
    # Count total surviving trees
    result = sum(len(trees[r][c]) for r in range(N) for c in range(N))
    print(result)

if __name__=="__main__":
    main()
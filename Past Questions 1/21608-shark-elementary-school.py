import collections
import heapq

def main():
    N = int(input().strip())
    # Map each student to a list of favorite students
    students_map = collections.defaultdict(list)
    classroom = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(N ** 2):
        row = list(map(int, input().strip().split(" ")))
        # Key: student, Value: list of favorite students
        students_map[row[0]] = row[1:]

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Function to find the best seat for the given student
    def search(key):
        nonlocal directions
        potential_seats = []

        for r in range(N):
            for c in range(N):
                # Seat is empty
                if not classroom[r][c]:
                    like_count = empty_count = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            # Check if there's a favorite student in the adjacent seat
                            if classroom[nr][nc] in students_map[key]:
                                like_count += 1
                            # Check if the adjacent seat is empty
                            if not classroom[nr][nc]:
                                empty_count += 1
                    # Max heap (automatically satisfies conditions 1-3)
                    heapq.heappush(potential_seats, (-like_count, -empty_count, r, c))

         # Pop the seat with highest like_count → highest empty_count → smallest row → smallest col
        _, _, best_r, best_c = heapq.heappop(potential_seats)

        return best_r, best_c

    # Place each student one by one in the optimal seat
    for key in students_map:
        r, c = search(key)
        classroom[r][c] = key
    
    satisfaction_map = { 0 : 0, 1 : 1, 2 : 10, 3 : 100, 4 : 1000 }
    like_counts = []

    # Calculate total satisfaction score
    for r in range(N):
        for c in range(N):
            like_count = 0
            student = classroom[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and classroom[nr][nc] in students_map[student]:
                    like_count += 1
            like_counts.append(like_count)

    satisfaction = 0
    for likes in like_counts:
        satisfaction += satisfaction_map[likes]

    print(satisfaction)

if __name__=="__main__":
    main()
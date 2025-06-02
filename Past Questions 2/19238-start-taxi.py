from collections import deque
import heapq

def main():
    N, M, K = map(int, input().strip().split(" "))
    grid = [list(map(int, input().strip().split(" "))) for _ in range(N)]
    R, C = map(int, input().strip().split(" "))
    taxi_r, taxi_c = R - 1, C - 1

    # Store passengers’ start and destination positions
    start_positions = []
    end_positions = []

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().strip().split())
        start_positions.append((x1 - 1, y1 - 1))
        end_positions.append((x2 - 1, y2 - 1))
    
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] 

    # Calculate all reachable passenger distances from taxi’s current location
    def find_nearest_passenger(x, y):
        nonlocal K

        q = deque([(x, y, 0)])
        visited = set([(x, y)])

        candidates = []
        min_dist = None

        while q:
            r, c, d = q.popleft()
            
            # Stop search if distance already exceeded closest candidate
            if min_dist is not None and d > min_dist:
                break
            
            # If a passenger is found at this position
            if (r, c) in start_positions:
                heapq.heappush(candidates, (r, c))
                min_dist = d

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 1 and (nr, nc) not in visited: 
                    q.append((nr, nc, d + 1))
                    visited.add((nr, nc))

        # No reachable passenger found
        if not candidates:
            return None, -1
        
        # Return passenger with smallest row, then column
        r, c = heapq.heappop(candidates)
        return (r, c), min_dist

    # Attempt to deliver a passenger from (start_r, start_c) to their destination
    def deliver_passenger(start_r, start_c):
        nonlocal K, taxi_r, taxi_c
        end_r = end_c = 0

        # Find the destination for this passenger
        idx_to_remove = 0
        for i in range(len(start_positions)):
            if start_positions[i] == (start_r, start_c):
                end_r, end_c = end_positions[i]
                idx_to_remove = i
                break

        q = deque([(start_r, start_c, 0, K)])
        visited = set([(start_r, start_c)])

        while q:
            r, c, d, f = q.popleft()  

            # Out of fuel
            if not f:
                return False
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 1 and (nr, nc) not in visited:
                    # If destination reached
                    if (nr, nc) == (end_r, end_c):
                        # Refill fuel after successful delivery
                        f += ((d + 1) * 2) - 1
                        K = f
                        taxi_r, taxi_c = end_r, end_c
                        
                        # Remove both positions from the array to find the next nearest passenger
                        start_positions.pop(idx_to_remove)
                        end_positions.pop(idx_to_remove)
                        return True
                    
                    q.append((nr, nc, d + 1, f - 1))
                    visited.add((nr, nc))
        
        # Could not reach destination
        return False

    # Main simulation loop: repeat M times (once per passenger)
    for _ in range(M):   
        passenger_pos, dist = find_nearest_passenger(taxi_r, taxi_c)
        
        # Cannot find or reach any passenger
        if passenger_pos is None or K < dist:
            print(-1)
            return
      
        r, c = passenger_pos

        # Deduct fuel to get to the passenger
        K -= dist

        # Out of fuel when delivering the passenger
        if not deliver_passenger(r, c):
            print(-1)
            return

    print(K)

if __name__=="__main__":
    main()
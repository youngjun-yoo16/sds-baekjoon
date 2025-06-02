from collections import deque

def main():
    N, K = map(int, input().strip().split(" "))
    A = deque(map(int, input().strip().split(" ")))
    # Tracks where robots are on the top N positions of the belt
    robots = deque(0 for _ in range(N))

    # Helper function to count how many belt cells have durability 0
    def checkZero(A):
        zero = 0
        for belt in A:
            if not belt:
                zero += 1
                if zero >= K:
                    return True
        
        return False
    
    turn = 0

    # Run until there are at least K belt positions with 0 durability
    while not checkZero(A):
        # Step 1: Rotate both the belt and the robots
        A.rotate()
        robots.rotate()

        # After rotation, if a robot is at the end (unloading position), remove it
        if robots[N - 1]:
            robots[N - 1] = 0

        # Step 2: Move robots forward if possible
        # Move from second-to-last to first (right to left), so earlier robots move first
        for i in range(N - 2, -1, -1):
            # Move if:
            # - There's a robot at position i
            # - Next cell has no robot
            # - Next belt section has durability
            if robots[i] and not robots[i + 1] and A[i + 1]:
                robots[i], robots[i + 1] = robots[i + 1], robots[i]
                A[i + 1] -= 1
                # If robot reached unloading position, remove it
                if i + 1 == N - 1:
                    robots[i + 1] = 0
            
        # Step 3: Place new robot at the start if possible
        if A[0] and not robots[0]:
            robots[0] = 1
            A[0] -= 1

        turn += 1

    print(turn)

if __name__=="__main__":
    main()
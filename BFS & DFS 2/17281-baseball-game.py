import sys
import itertools

'''
1. Generate all permutations of the batting order (excluding player 0).
2. Fix player 0 as the 4th batter (index 3).
3. For each inning:
   - Reset outs and base states.
   - Use the batting order to simulate base running:
     * Single: move all runners forward one base.
     * Double: move all runners forward two bases.
     * Triple: move all runners forward three bases.
     * Home run: all runners score.
'''

def main():
    N = int(sys.stdin.readline().strip())
    record = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    max_score = 0
    
    # Generate all permutations of players 1 to 8 (player 0 will be inserted at position 3)
    for player in itertools.permutations(range(1, 9), 8):
        player = list(player)
        # Fix player 0 as the 4th batter (index 3)
        player.insert(3, 0)
        score = 0
        # Current batter index (0–8)
        p = 0

        # Simulate each inning
        for i in range(N):
            out = base1 = base2 = base3 = 0
            while out < 3:
                # Current batter's result this inning
                result = record[i][player[p]]

                if result == 0:
                    out += 1
                elif result == 1:
                    # Single hit
                    score += base3
                    base3 = base2
                    base2 = base1
                    base1 = 1
                elif result == 2:
                    # Double hit
                    score += base3 + base2
                    base3 = base1
                    base2 = 1
                    base1 = 0
                elif result == 3:
                    # Triple hit
                    score += base3 + base2 + base1
                    base3 = 1
                    base2 = base1 = 0
                else:
                    # Home run
                    score += base3 + base2 + base1 + 1
                    base3 = base2 = base1 = 0

                # Move to next batter
                p = (p + 1) % 9
        
        max_score = max(max_score, score)

    print(max_score)

if __name__=="__main__":
    main()
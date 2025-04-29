import sys
import collections

def main():
    N = int(sys.stdin.readline())

    if N == 1:
        print("1")
        
    q = collections.deque()
    for i in range(1, N + 1):
        q.append(i)

    # continue until only one card is left
    while len(q) != 1:
        # discard the topmost card
        q.popleft()

        # check if only one card remains after discarding
        if len(q) == 1:
            print(q.popleft())
            break

        # move the next topmost card to the bottom of the deck
        card = q.popleft()
        q.append(card)


if __name__=="__main__":
    main()
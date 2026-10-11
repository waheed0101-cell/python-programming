# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    x = int(input())
    sizes = Counter(map(int, input().split()))
    n = int(input())

    earned = 0
    for _ in range(n):
        size, price = map(int, input().split())
        if sizes[size] > 0:
            earned += price
            sizes[size] -= 1

    print(earned)

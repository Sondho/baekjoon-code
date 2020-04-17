import random

n, x = map(int, input().split())

sequence = random.sample(range(1, 11), n)
for item in range(0, n):
    print(sequence[item], end=' ')
print()
for item in range(0, n):
    if sequence[item] < x:
        print(sequence[item], end=' ')
    else:
        None
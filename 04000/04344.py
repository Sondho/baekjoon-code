count = int(input())
for i in range(count):
    x, *score = map(int, input().split())
    average = sum(score)/len(score)
    good = 0
    for j in score:
        if j > average:
            good += 1
    rate = good/len(score)*100
    print("%.3f" %rate, end='')
    print('%')


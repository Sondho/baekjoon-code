x = map(int, input())
count = 0
max = x[0]
for i in x:
    count += 1
    if max < i:
        max = i
        index = count
print(max)
print(index)
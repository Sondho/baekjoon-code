mul = 1
for input_number in range(3):
    number = int(input())
    mul *= number

list_count = []
for j in map(int, str(mul)):
    list_count.append(j)

for number_counting in range(10):
    print(list_count.count(number_counting))
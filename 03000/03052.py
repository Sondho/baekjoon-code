list_number = []
for i in range(10):
    input_number = int(input())
    list_number.append(input_number%42)

print(len(list(set(list_number))))

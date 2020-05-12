list_gk = []
list_char = []
for count in range(0, int(input())): # 단어의 개수 N
    list_char.append(list(map(str, input()))) # 단어를 list_char에 append

for input_char in list_char:
    group_check = True
    for alpha in list(set(input_char)):
        if len(input_char) == 1:
            break
        index_char = input_char.index(alpha)
        for i in range(index_char+1, len(input_char)):
            if input_char[i] != input_char[index_char]:
                if input_char[i:].count(input_char[index_char]) > 0:
                    group_check = False
                    break
                else:
                    break
        if group_check == False:
            break
    if group_check == True:
        list_gk.append(''.join(input_char))
print(len(list_gk))
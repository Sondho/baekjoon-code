# key=word.find를 매개변수로 word를 sorted 했을 때,
# 입력한 word와 일치하면 그룹단어
result = 0
for i in range(int(input())):
    word = input()
    print(f"list({word}) = {list(word)}")
    print(f"sorted({word}) = {sorted(word)}")
    print(f"sorted({word}, key=word.find) = {sorted(word, key=word.find)}")
    if list(word) == sorted(word): 
        result += 1
print(result)

# key=word.find ? -> word의 위치 그대로 정렬해줌.
# 문자열 위치알려주기(find) ?
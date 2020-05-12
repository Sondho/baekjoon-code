list_ch = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

input_char = input()
result = 0
for croatia in list_ch:
    if croatia in input_char:
        count = input_char.count(croatia)
        input_char = input_char.replace(croatia, ',')
        result += count
        
input_char = input_char.replace(',', '')
print(result + len(input_char))
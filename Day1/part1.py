total_sum = 0
with open('input.txt') as f:
    for line in f:
        str_num = ''
        for char in line.strip():
            if char.isdigit():
                str_num += char
                break
        for char in line.strip()[::-1]:
            if char.isdigit():
                str_num += char
                break
        total_sum += int(str_num)

print(total_sum)

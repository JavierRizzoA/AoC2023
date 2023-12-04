numbers = [
        'ZERO',
        'ONE',
        'TWO',
        'THREE',
        'FOUR',
        'FIVE',
        'SIX',
        'SEVEN',
        'EIGHT',
        'NINE',
]

def find_first_digit(string, reverse=False):
    norm_string = line.strip().upper()
    r = range(len(norm_string))
    if reverse:
        r = reversed(r)
    for i in r:
        if norm_string[i].isdigit():
            return norm_string[i]
        
        for j in range(len(numbers)):
            if norm_string[i:].startswith(numbers[j]):
                return str(j)


total_sum = 0
with open('input.txt') as f:
    for line in f:
        n = int(find_first_digit(line) + find_first_digit(line, reverse=True))
        total_sum += n


print(total_sum)

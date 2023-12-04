lines = None
with open('input.txt') as f:
    lines = [line.strip() for line in f]


total = 0
for i in range(len(lines)):
    check_start = None
    check_end = None
    part_number = ''
    valid = False
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            part_number += lines[i][j]
            if check_start is None:
                check_start = max(0, j - 1)
        if not lines[i][j].isdigit() or j == len(lines[i]) - 1:
            if check_start is not None:
                check_end = min(len(lines[i]), j + 1)
                for y in range(max(0, i - 1), min(len(lines), i + 1 + 1)):
                    for x in range(check_start, check_end):
                        if not lines[y][x].isdigit() and not lines[y][x] == '.':
                            total += int(part_number)
                            valid = True
                            break
                    if valid:
                        break
                check_start = None
                check_end = None
                part_number = ''
                valid = False


print(total)

total = 0


with open('input.txt') as f:
    for line in f:
        card, numbers = line.strip().replace('  ', ' ').split(': ')
        winning, have = numbers.split(' | ')
        winning = winning.split(' ')
        have = have.split(' ')

        wins = 0
        for h in have:
            if h in winning:
                wins += 1

        if wins > 0:
            total += 2 ** (wins - 1)


print(total)

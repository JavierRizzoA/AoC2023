cards = {}
instances = {}


with open('input.txt') as f:
    for line in f:
        card, numbers = line.strip().replace('  ', ' ').split(': ')
        winning, have = numbers.split(' | ')
        winning = winning.split(' ')
        have = have.split(' ')
        card = int(card.replace('  ', ' ').split(' ')[1])

        wins = 0
        for h in have:
            if h in winning:
                wins += 1

        cards[card] = wins
        instances[card] = 1


for c in cards:
    for i in range(c + 1, c + 1 + cards[c]):
        if i not in instances:
            break
        instances[i] += instances[c]


total = 0
for i in instances.values():
    total += i


print(total)

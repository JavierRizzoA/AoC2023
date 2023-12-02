total = 0


with open('input.txt') as f:
    for line in f:
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}

        game_id, values = line.strip().split(': ')
        game_n = int(game_id.split(' ')[1])
        games = values.split('; ')

        for game in games:
            for cube in game.split(', '):
                number, color = cube.split(' ')
                number = int(number)
                min_cubes[color] = max(number, min_cubes[color])

        total += min_cubes['red'] * min_cubes['blue'] * min_cubes['green']


print(total)

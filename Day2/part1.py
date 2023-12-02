RED = 12
GREEN = 13
BLUE = 14

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

        if (min_cubes['red'] <= RED
                and min_cubes['green'] <= GREEN
                and min_cubes['blue'] <= BLUE):
            total += game_n


print(total)

sailors = [input(f'Моряк {i + 1}: ').split() for i in range(int(input('Введите количество моряков: ')))]
team_1 = [s[0] for s in sailors if int(s[1]) > 40 or int(s[1]) < 20]
team_2 = set([s[0] for s in sailors]) - set(team_1)
print('Команда 1: ' + ', '.join(sorted(team_1)))
print('Команда 2: ' + ', '.join(sorted(team_2)))
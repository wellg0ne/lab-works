import csv
from os.path import isfile
from os import remove, listdir

s = ['Номер', 'Задача', 'Время', 'Дата', 'Приоритет', 'Статус']


def sorter(note, key):
    if key == 'Приоритет':
        if note[4] == '(Очень важно)':
            return 0
        elif note[4] == '(Важно)':
            return 1
        elif note[4] == '(Не важно)':
            return 2
    elif key == 'Статус':
        if note[5] == 'Не выполнено':
            return 0
        elif note[5] == 'В процессе':
            return 1
        elif note[5] == 'Выполнено':
            return 2
    else:
        return note[s.index(key)]


def get_list(key):
    for x in listdir('notebooks'):
        if isfile(f'notebooks/{x}'):
            print(x)

            with open(f'notebooks/{x}', 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
                print('\n'.join([', '.join(x) for x in sorted([x.split(',') for x in lines], key=lambda x: sorter(x, key))]) + '\n')


def create_notebook(name):
    i = 1
    lines = []

    with open(f'notebooks/{name}', 'w', encoding='utf-8') as f:
        print('Вводите строчки одну за другой: ')

        while True:
            try:
                lines.append(f'{i},{input()}')
                i += 1
            except KeyboardInterrupt:
                break

        f.write('\n'.join(lines))

    print('Выполнено!')


def edit_notebook(name):
    with open(f'notebooks/{name}', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    line = input('Введите номер строки: ')
    lines[int(line) - 1] = input('Введите строку: ')

    with open(f'notebooks/{name}', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print('Выполнено!')


def add_note(name):
    with open(f'notebooks/{name}', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    with open(f'notebooks/{name}', 'a', encoding='utf-8') as f:
        f.write(f'\n{max([int(x[0]) for x in lines]) + 1},{input("Введите строку: ")}')

    print('Выполнено!')


def delete_notebook(name):
    remove(f'notebooks/{name}')

    print('Выполнено!')


def main():
    while True:
        try:
            task = input('Введите задание: ')
            if task == 'Список':
                get_list(input('Введите сортировку: '))
            elif task == 'Создать':
                create_notebook(input('Введите название файла: '))
            elif task == 'Изменить':
                edit_notebook(input('Введите название файла: '))
            elif task == 'Добавить':
                add_note(input('Введите название файла: '))
            elif task == 'Удалить':
                delete_notebook(input('Введите название файла: '))
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()

lst_numbers = [int(x) for x in input('Введите числа через пробел: ').split()]
if len(lst_numbers) < 4: print('Введено менее четырёх чисел')
else: print([n for n in lst_numbers if n > min(lst_numbers) and n < max(lst_numbers)])
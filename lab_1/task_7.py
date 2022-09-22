p = input('Введите PIN-код: ')
if p.isdigit() and len(p) in [4, 6]: print('OK')
else: print('ERROR')
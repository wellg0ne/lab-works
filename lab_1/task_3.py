s = input('Введите строку: ')
if len(s) >= 3: s += s.endswith('ing') and 'ly' or 'ing'
print(s)
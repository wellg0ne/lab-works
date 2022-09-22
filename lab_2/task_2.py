numbers = [5, 215, 52, 98, 654, 15887, 1, 3215]
print([n % 2 == 0 and n * min(numbers) or n * max(numbers) for n in numbers])
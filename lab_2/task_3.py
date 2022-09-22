import random
n, n_min, n_max = 100000, -5, 5
numbers = [random.uniform(-10, 10) for _ in range(n)]
print(numbers)
print(len([x for x in numbers if x >= n_min and x < n_max]))
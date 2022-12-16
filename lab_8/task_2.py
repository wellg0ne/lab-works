import matplotlib.pyplot as plt
import numpy as np

labels = ['Винегрет овощной', 'Суп', 'Котлеты', 'Гречка', 'Чай', 'Тортик']
numbers = np.array([100, 150, 200, 140, 20, 450])


def value(v):
    return f'{np.round(v/100.*numbers.sum())} ккал'


if __name__ == '__main__':
    plt.pie(numbers, labels=labels, startangle=90, autopct=value)
    plt.title('Калорийность обеда:')
    plt.show()

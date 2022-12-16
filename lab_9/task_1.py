import pandas as pd
import matplotlib.pyplot as plt

passangers = pd.read_csv('titanic.csv')

middleaged = passangers[(passangers['Age'] > 30) & (passangers['Age'] < 40) & (passangers['Sex'] == 'male')]
survived = passangers[((passangers['Survived'] == 1) & (passangers['Pclass'] == 1)) | ((passangers['Sex'] == 'female') & (passangers['Age'] < 25))]
young = passangers[(passangers['Age'] < 25)]

survived = survived.groupby(['Sex', 'Pclass']).size()
young = young.groupby(['Sex', 'Pclass', 'Survived']).size()


if __name__ == '__main__':
    survived.plot.bar()
    young.plot.bar()
    plt.show()

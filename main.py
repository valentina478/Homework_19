import pandas as pd
import matplotlib.pyplot as plt
import random

data = {
    'Name': ['Emily', 'Liam', 'Sophia', 'Jackson', 'Olivia', 'John', 'Anna', 'William', 'Mia', 'Benjamin'],
    'Age': [25, 32, 18, 40, 29, 50, 22, 36, 27, 45],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Score': [97, 92, 91, 85, 80, 96, 78, 89, 84, 68]
}
df = pd.DataFrame(data) # task_1


def task_2():
    plt.bar(data['Name'], data['Score'], label='Оцінки студентів')
    plt.xlabel('Ім\'я')
    plt.ylabel('Оцінка')
    plt.legend()
    plt.show()
task_2()

print(df[:5]) # task_3

def task_4():
    x = [random.randint(0, 100) for _ in range(100)]
    y = [e * 2 + random.randint(0, 100) for e in x]

    plt.scatter(x, y, label='Діаграма розсіювання')
    plt.xlabel('Вісь X')
    plt.ylabel('Вісь Y')
    plt.legend()
    plt.show()
task_4()


def task_5():

    plt.bar(data['Gender'], data['Score'])
    plt.xlabel('Стать')
    plt.ylabel('Оцінка')
    plt.title('Порівняння оцінок за категоріями')
    plt.show()
task_5()

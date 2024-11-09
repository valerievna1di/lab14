import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з файлу population.csv
data = pd.read_csv('population.csv')

# Відокремлення даних для кожної країни
ukraine_data = data[data['Country Name'] == 'Ukraine']
uk_data = data[data['Country Name'] == 'United Kingdom']

# Витягнення значень років і чисельності населення для кожної країни
x = ukraine_data['Time'].values  # Роки
y = ukraine_data['Value'].values  # Дані для України
z = uk_data['Value'].values       # Дані для Великої Британії

# Створення лінійного графіка
plt.figure(figsize=(10, 6))

# Лінійний графік для Великої Британії
plt.plot(x, z, label='United Kingdom', color="purple")
# Додавання точок для Великої Британії
plt.scatter(x, z, color="purple")

# Лінійний графік для України
plt.plot(x, y, label='Ukraine', color="blue")
# Додавання точок для України
plt.scatter(x, y, color="blue")

# Назва графіка та підписи осей
plt.title('Population, total for Ukraine and United Kingdom', fontsize=15)
plt.xlabel('Year', fontsize=12, color='red')
plt.ylabel('Indicator', fontsize=12, color='red')

# Відображення легенди
plt.legend()

# Додавання сітки
plt.grid(True)

# Налаштування осі X для відображення лише цілих значень років
plt.xticks(x, rotation=45)

# Відображення графіка
plt.show()

# 2.2 Побудова стовпчастої діаграми для обраної користувачем країни
def plot_bar_chart(country, x, y, z):
    # Вибір даних залежно від країни
    if country == "Ukraine":
        values = y
        color = "blue"
    elif country == "United Kingdom":
        values = z
        color = "purple"
    else:
        print("Invalid country. Please choose either 'Ukraine' or 'United Kingdom'.")
        return

    # Побудова стовпчастої діаграми
    plt.figure(figsize=(8, 5))
    plt.bar(x, values, color=color)

    # Налаштування осей і заголовків
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(f'Population Indicator for {country}')
    plt.show()

# Введення країни для стовпчастої діаграми
country_for_bar_chart = input("Enter the name of the country for the bar chart (Ukraine or United Kingdom): ")
plot_bar_chart(country_for_bar_chart, x, y, z)

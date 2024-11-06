import numpy as np
import matplotlib.pyplot as plt 

# Дані для графіка
x = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
y = [47812949, 47451626, 47105171, 46787786, 46509355, 46258189, 46053331, 45870741, 45706086, 45593342, 45489648, 45272155, 45167350, 45038236, 44880758, 44690584, 44474512, 44207754, 43848986, 38000000, 37000000]  # Дані для України
z = [59647577, 59987905, 60401206, 60846820, 61322463, 61806995, 62276270, 62766365, 63258810, 63700215, 64128273, 64602298, 65116219, 65611593, 66058859, 66460344, 66836327, 67081234, 67026292, 67791000, 68350000]  # Дані для Великої Британії

# Перетворення списків на масиви NumPy
x = np.array(x)
y = np.array(y)
z = np.array(z)

# Створення графіка
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
plt.title('Population, total for Ukraine and United Kingdom', fontsize=15)  # Назва графіка
plt.xlabel('Year', fontsize=12, color='red')  # Підпис осі X
plt.ylabel('Indicator', fontsize=12, color='red')  # Підпис осі Y

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
import matplotlib.pyplot as plt

# Дані про розподіл поїздів через певну станцію
train_types = ['Пасажирський', 'Вантажний', 'Швидкісний', 'Міжміський']
train_counts = [150, 200, 50, 100]  # Кількість поїздів кожного типу

# Побудова кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(train_counts, labels=train_types, autopct='%1.1f%%', startangle=140, 
        colors=['skyblue', 'orange', 'lightgreen', 'salmon'])

# Додавання заголовку
plt.title('Типи поїздів, що проходять через станцію')

# Відображення діаграми
plt.show()
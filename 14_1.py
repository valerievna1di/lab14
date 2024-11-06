# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:20:22 2024

@author: diyak
"""

import numpy as np
import matplotlib.pyplot as plt

# Оголошення функції
def Y(x):
    # Обробка точки x=0, щоб уникнути ділення на нуль
    return np.sin(x) * (1 / x) * np.cos(x**2 + 1 / x) if x != 0 else 0

# Генеруємо значення x у проміжку [-2, 2] з достатньою кількістю точок
x = np.linspace(-2, 2, 200)
y = np.array([Y(xi) for xi in x])

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', linewidth=2, linestyle='-', label=r'$Y(x) = \sin(x) \cdot \frac{1}{x} \cdot \cos(x^2 + \frac{1}{x})$')

# Настройки осей і графіка
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Графік функції Y(x)')
plt.legend()
plt.grid(True)

# Відображення графіка
plt.show()

import matplotlib.pyplot as plt


"""Matplotlib — это библиотека для визуализации данных в Python. 
              Она используется для создания любых видов графиков: 
         линейных, круговых диаграмм, построчных гистограмм и других — в зависимости от задач"""

fig, ax = plt.subplots(figsize=(6, 4.7), layout='constrained')
ax.axis([0, 15, 0, 15])
X = [2, 4, 6, 8, 10, 12, 14]
Y = [5, 6, 8, 12, 11, 9, 4]
ax.annotate('Максимальное значение', xy=(8, 12), xytext=(1, 12),
            arrowprops=dict(facecolor='r', shrink=0.1))

ax.bar(X, Y)
plt.title('Прирост тока по позициям')
plt.xlabel('Позиция')
plt.ylabel('Ток')
plt.show()
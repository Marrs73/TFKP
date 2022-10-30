import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
from math import*

sup_x = 2
inf_x = -1
sup_y = pi
inf_y = 0 
step = 0.01
Dots_count = 10_000

def exponent_area(x_list, y_list, coeff):
    listik_result_x = list()
    listik_result_y = list()
    i = 0
    while (i < ((abs(inf_x) + abs(sup_x))*int(1/step))**2):
        listik_result_x.append(e**(x_list[i] * coeff) * cos(y_list[i] * coeff))
        listik_result_y.append(e**(x_list[i] * coeff) * sin(y_list[i] * coeff))
        i += 1

    return listik_result_x, listik_result_y

def exponent(universe, coeff):
    listik_result_x = list()
    listik_result_y = list()
    for i in range(Dots_count):
        listik_result_x.append(e**(universe[i][0] * coeff) * cos(universe[i][1] * coeff))
        listik_result_y.append(e**(universe[i][0] * coeff) * sin(universe[i][1] * coeff))

    return listik_result_x, listik_result_y

def shift(universe, value_x, value_y):
    listik_result_x = list()
    listik_result_y = list()
    for i in range(Dots_count):
        listik_result_x.append(universe[i][0] + value_x)
        listik_result_y.append(universe[i][1] + value_y)

    return listik_result_x, listik_result_y

def logarithm(universe, coeff):
    listik_result_x = list()
    listik_result_y = list()
    for i in range(Dots_count):
        listik_result_x.append(log((universe[i][0] * coeff)**2 + (universe[i][1] * coeff)**2)/2)
        if ((universe[i][0] >= 0 and universe[i][1] >= 0) or (universe[i][1] <= 0 and universe[i][0] >= 0)):
            listik_result_y.append(atan(universe[i][1]/universe[i][0]))
        elif (universe[i][0] <= 0 and universe[i][1] >= 0):
            listik_result_y.append(atan(universe[i][1]/universe[i][0]) + pi)
        else:
            listik_result_y.append(atan(universe[i][1]/universe[i][0]) - pi)
    return listik_result_x, listik_result_y

def scale(universe, coeff):
    listik_result_x = list()
    listik_result_y = list()
    for i in range(Dots_count):
        listik_result_x.append(universe[i][0] * coeff)
        listik_result_y.append(universe[i][1] * coeff)

    return listik_result_x, listik_result_y

def example():
    # Задание параметров
    H = 5
    V0 = 2
    fig = plt.figure(figsize=(12,6))
    gs = GridSpec(ncols=3, nrows=2, figure=fig)

    listik = np.linspace(0, 10, num = Dots_count)
    #listik2 = np.linspace(0, 10, num = Dots_count)
    listik2 = np.array([H for _ in range(0, Dots_count)])

    # вызов преобразований
    ax1 = plt.subplot(gs[0, 0])
    ax1.grid()
    ax1.scatter(listik, listik2, color="#ff0000", s=2)
    ax1.scatter(-10, 8, color="#ffffff", s=6)
    ax1.scatter(10, 8, color="#ffffff", s=6)


    ax2 = plt.subplot(gs[0, 1])
    universe = list(zip(listik, listik2))
    ax2.grid()
    x, y = exponent(universe, pi/H)
    ax2.scatter(x, y, color="#ff0000", s=2)
    ax2.scatter(0, 2, color="#ff0000", s=6)
    ax2.scatter(-10, 8, color="#ffffff", s=6)
    ax2.scatter(10, 8, color="#ffffff", s=6)

    ax3 = plt.subplot(gs[0, 2])
    universe = list(zip(x, y))
    x, y = shift(universe, 1, 0)
    ax3.grid()
    ax3.scatter(x, y, color="#ff0000", s=2)
    ax3.scatter(0, 2, color="#ff0000", s=6)
    ax3.scatter(-10, 8, color="#ffffff", s=6)
    ax3.scatter(10, 8, color="#ffffff", s=6)

    ax4 = plt.subplot(gs[1, 0])
    universe = list(zip(x, y))
    x, y = logarithm(universe, 1)
    ax4.grid()
    ax4.scatter(x, y, color="#ff0000", s=2)
    ax4.scatter(0, 2, color="#ff0000", s=6)
    ax4.scatter(-10, 8, color="#ffffff", s=6)
    ax4.scatter(10, 8, color="#ffffff", s=6)

    ax5 = plt.subplot(gs[1, 1])
    universe = list(zip(x, y))
    ax5.grid()
    x, y = scale(universe, V0/pi)
    ax5.scatter(x, y, color="#ff0000", s=2)
    ax5.scatter(0, 2, color="#ff0000", s=6)
    ax5.scatter(-10, 8, color="#ffffff", s=6)
    ax5.scatter(10, 8, color="#ffffff", s=6)
    # universe = list(zip(x, y))
    # x, y = shift(universe, 0, -5)

    plt.show()

#example()
x = list()
y = list()
i, j = inf_x, inf_y

while (i <= sup_x):
    j = inf_y
    while (j <= sup_y):
        x.append(i)
        y.append(j)
        j += step
    i += step

#print(((abs(inf) + abs(sup))*int(1/step))**2)
#print(len(x))
x, y = exponent_area(*exponent_area(x, y, 1), 1)
plt.scatter(x, y, color="#aa0000", s=10)
plt.show()
#print(y)
# print(x)
print(len(x))
# print( ((abs(inf) + abs(sup))*int(1/step) + 1)**2 )

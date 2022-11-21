# "cmp" stands for CoMplex Plotting
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
from math import*


class graph():
    x_list, y_list = None, None
    colour = None
    size = None

    def create_rectangle_set(self, inf_x, inf_y, sup_x, sup_y, step_x=1, step_y=1):  
        x = np.arange(inf_x, sup_x + step_x/10, step_x).repeat(int((sup_y - inf_y)*int(1/step_y) + 1))
        y_start = np.arange(inf_y, sup_y + step_y/10, step_y)
        y = y_start.copy()

        for _ in range((sup_x - inf_x)*int(1/step_x)):
            y = np.concatenate((y, y_start))

        self.x_list, self.y_list = x, y

    def shift(self, real_val=0, imag_val=0): 
        self.x_list += real_val
        self.y_list += imag_val

    def scale(self, real_val=1, imag_val=0):
        x_res = self.x_list * real_val - self.y_list * imag_val
        y_res = self.x_list * imag_val + self.y_list * real_val
        self.x_list, self.y_list = x_res, y_res

    def exponent(self, real_coeff=1, imag_coeff=0):
        x_res = e**(self.x_list * real_coeff - self.y_list * imag_coeff) * np.cos(real_coeff * self.y_list + imag_coeff * self.x_list)
        y_res = e**(self.x_list * real_coeff - self.y_list * imag_coeff) * np.sin(real_coeff * self.y_list + imag_coeff * self.x_list)

        self.x_list, self.y_list = x_res, y_res

    def plot(self, colour=None, size=None):
        if (colour == None):
            if (self.colour != None): colour = self.colour
            else: colour = "#ff0000"

        if (size == None):
            if (self.size != None): size = self.size
            else: size = 4

        plt.scatter(self.x_list, self.y_list, color=colour, s=size)

    def logarithm(self, coeff=1):
        x_res = self.x_list.copy()
        y_res = self.y_list.copy()

        for i in range(len(self.x_list)):
            x_res[i] = log((self.x_list[i] * coeff)**2 + (self.y_list[i] * coeff)**2)/2
            y_res[i] = arg(self.x_list[i], self.y_list[i])

        self.x_list, self.y_list = x_res, y_res 
    
    def sin(self):
        x_res = exponent(self.x_list, self.y_list, 0, 1)[0] - exponent(self.x_list, self.y_list, 0, -1)[0]
        y_res = exponent(self.x_list, self.y_list, 0, 1)[1] - exponent(self.x_list, self.y_list, 0, -1)[1]
        x_res, y_res = scale(x_res, y_res, 0, 0.5)

        self.x_list, self.y_list = x_res, y_res

    def cos(self):
        x_res = exponent(self.x_list, self.y_list, 0, 1)[0] + exponent(self.x_list, self.y_list, 0, -1)[0]
        y_res = exponent(self.x_list, self.y_list, 0, 1)[1] + exponent(self.x_list, self.y_list, 0, -1)[1]
        x_res, y_res = scale(x_res, y_res, 0.5)

        self.x_list, self.y_list = x_res, y_res
        
def exponent(x_list, y_list, real_coeff=1, imag_coeff=0): # already with numpy
    x_res = e**(x_list * real_coeff - y_list * imag_coeff) * np.cos(real_coeff * y_list + imag_coeff * x_list)
    y_res = e**(x_list * real_coeff - y_list * imag_coeff) * np.sin(real_coeff * y_list + imag_coeff * x_list)

    return x_res, y_res

def shift(x_list, y_list, real_val=0, imag_val=0): # already with numpy
    x_list += real_val
    y_list += imag_val

    return x_list, y_list

def logarithm_oldest(universe, coeff=1): # shouldn't be with numpy by definition
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

def logarithm_old(x_list, y_list, coeff=1): # already with numpy
    x_res = x_list.copy()
    y_res = y_list.copy()

    for i in range(len(x_list)):
        x_res[i] = log((x_list[i] * coeff)**2 + (y_list[i] * coeff)**2)/2
        if ((x_list[i] >= 0 and y_list[0] >= 0) or (y_list[0] <= 0 and x_list[i] >= 0)):
            y_res[i] = atan(y_list[i]/x_list[i])
        elif (x_list[i] <= 0 and y_list[i] >= 0):
            y_res[i] = atan(y_list[i]/x_list[i]) + pi
        else:
            y_res[i] = atan(y_list[i]/x_list[i]) - pi

    return x_res, y_res

def logarithm(x_list, y_list, coeff=1): # newest version with arg()
    x_res = x_list.copy()
    y_res = y_list.copy()

    for i in range(len(x_list)):
        x_res[i] = log((x_list[i] * coeff)**2 + (y_list[i] * coeff)**2)/2
        y_res[i] = arg(x_list[i], y_list[i])

    return x_res, y_res

def scale(x_list, y_list, real_val=1, imag_val=0): # already with numpy
    x_res = x_list * real_val - y_list * imag_val
    y_res = x_list * imag_val + y_list * real_val
    return x_res, y_res

def example(): # already with numpy
    # Задание параметров
    H = 5
    V0 = 2
    fig = plt.figure(figsize=(12,6))
    gs = GridSpec(ncols=3, nrows=2, figure=fig)

    x_list, y_list = create_rectangle_set(-5, 0, 5, H, 0.01, 0.01)
    x_list2, y_list2 = np.arange(0, 5, 0.01), np.full(500, H)

    # вызов преобразований
    ax1 = plt.subplot(gs[0, 0])
    ax1.grid()
    ax1.scatter(x_list, y_list, color="#ff0000", s=2)
    ax1.scatter(x_list2, y_list2, color="#0000ff", s=4)
    # ax1.scatter(-10, 8, color="#ffffff", s=6)
    # ax1.scatter(10, 8, color="#ffffff", s=6)


    ax2 = plt.subplot(gs[0, 1])
    ax2.grid()
    x_list, y_list = exponent(x_list, y_list, pi/H)
    x_list2, y_list2 = exponent(x_list2, y_list2, pi/H)
    ax2.scatter(x_list, y_list, color="#ff0000", s=2)
    ax2.scatter(x_list2, y_list2, color="#0000ff", s=4)
    # ax2.scatter(0, 2, color="#ff0000", s=6)
    # ax2.scatter(-10, 8, color="#ffffff", s=6)
    # ax2.scatter(10, 8, color="#ffffff", s=6)

    ax3 = plt.subplot(gs[0, 2])
    x_list, y_list = shift(x_list, y_list, 1, 0)
    x_list2, y_list2 = shift(x_list2, y_list2, 1, 0)
    ax3.grid()
    ax3.scatter(x_list, y_list, color="#ff0000", s=2)
    ax3.scatter(x_list2, y_list2, color="#0000ff", s=4)
    # ax3.scatter(0, 2, color="#ff0000", s=6)
    # ax3.scatter(-10, 8, color="#ffffff", s=6)
    # ax3.scatter(10, 8, color="#ffffff", s=6)

    ax4 = plt.subplot(gs[1, 0])
    x_list, y_list = logarithm(x_list, y_list, 1)
    x_list2, y_list2 = logarithm(x_list2, y_list2, 1)
    ax4.grid()
    ax4.scatter(x_list, y_list, color="#ff0000", s=2)
    ax4.scatter(x_list2, y_list2, color="#0000ff", s=4)
    # ax4.scatter(0, 2, color="#ff0000", s=6)
    # ax4.scatter(-10, 8, color="#ffffff", s=6)
    # ax4.scatter(10, 8, color="#ffffff", s=6)

    ax5 = plt.subplot(gs[1, 1])
    ax5.grid()
    x_list, y_list = scale(x_list, y_list, V0/pi)
    x_list2, y_list2 = scale(x_list2, y_list2, V0/pi)
    ax5.scatter(x_list, y_list, color="#ff0000", s=2)
    ax5.scatter(x_list2, y_list2, color="#0000ff", s=4)
    # ax5.scatter(0, 2, color="#ff0000", s=6)
    # ax5.scatter(-10, 8, color="#ffffff", s=6)
    # ax5.scatter(10, 8, color="#ffffff", s=6)

    plt.show()

def create_rectangle_set(inf_x, inf_y, sup_x, sup_y, step_x=1, step_y=1):  
    x = np.arange(inf_x, sup_x + step_x/10, step_x).repeat(int((sup_y - inf_y)*int(1/step_y) + 1))
    y_start = np.arange(inf_y, sup_y + step_y/10, step_y)
    y = y_start.copy()

    for _ in range((sup_x - inf_x)*int(1/step_x)):
        y = np.concatenate((y, y_start))

    return x, y

def sin(x_list, y_list):
    x_res = x_list.copy()
    y_res = y_list.copy()

    x_res, y_res = exponent(x_list, y_list, 0, 1)[0] - exponent(x_list, y_list, 0, -1)[0], exponent(x_list, y_list, 0, 1)[1] - exponent(x_list, y_list, 0, -1)[1]
    x_res, y_res = scale(x_res, y_res, 0, 0.5)

    return x_res, y_res

def cos(x_list, y_list):
    x_res = x_list.copy()
    y_res = y_list.copy()

    x_res, y_res = exponent(x_list, y_list, 0, 1)[0] + exponent(x_list, y_list, 0, -1)[0], exponent(x_list, y_list, 0, 1)[1] + exponent(x_list, y_list, 0, -1)[1]
    x_res, y_res = scale(x_res, y_res, 0.5)

    return x_res, y_res

def arg(x, y):
    if (x == 0):
        if (y == 0):
            res = None
        else:
            res = pi/2
    else:
        res = atan(y/x)
    
    return res

def mod(x, y):
    return sqrt(x**2 + y**2)

#TODO_LIST
# убедиться в рабоспособности всей библиотеки
# переписать её под ООП
# Добавить интеграцию с pyplot.gridspec
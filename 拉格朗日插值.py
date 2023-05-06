# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:28:47 2023

@author: 86319
"""

import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x):
    return np.cos(x)

# 取3个数据点
x_vals = np.linspace(5, 6, 3)
y_vals = f(x_vals)

# 计算插值多项式
def L(x, x_vals, y_vals):
    L_2 = 0
    for i in range(len(x_vals)):
        if i == 0:
            L_2 += y_vals[i] * ((x - x_vals[1]) * (x - x_vals[2])) / ((x_vals[0] - x_vals[1]) * (x_vals[0] - x_vals[2]))
        elif i == 1:
            L_2 += y_vals[i] * ((x - x_vals[0]) * (x - x_vals[2])) / ((x_vals[1] - x_vals[0]) * (x_vals[1] - x_vals[2]))
        elif i == 2:
            L_2 += y_vals[i] * ((x - x_vals[0]) * (x - x_vals[1])) / ((x_vals[2] - x_vals[0]) * (x_vals[2] - x_vals[1]))
    return L_2

# 计算pi/4, pi/2, 3pi/4, 7pi/4的函数值
x1 = np.pi/4
x2 = np.pi/2
x3 = 3*np.pi/4
x4 = 7*np.pi/4

print("pi/4的插值函数值：", L(x1, x_vals, y_vals))
print("pi/4的真值：", f(x1))
print("pi/2的插值函数值：", L(x2, x_vals, y_vals))
print("pi/2的真值：", f(x2))
print("3pi/4的插值函数值：", L(x3, x_vals, y_vals))
print("3pi/4的真值：", f(x3))
print("7pi/4的插值函数值：", L(x4, x_vals, y_vals))
print("7pi/4的真值：", f(x4))

# 绘制插值多项式和真实函数的图像
x = np.linspace(0, 8, 100)
y_interp = L(x, x_vals, y_vals)
y_true = f(x)
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.plot(x, y_interp, label='插值函数')
plt.plot(x, y_true, label='真实函数')
plt.scatter(x_vals, y_vals, label='数据点', color='red')
plt.legend()
plt.show()


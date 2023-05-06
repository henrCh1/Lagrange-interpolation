# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:37:29 2023

@author: 86319
"""

import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x):
    return np.cos(x)

# 取1000个数据点
x_vals = np.linspace(0, 8, 1000)
y_vals = f(x_vals)

# 计算插值多项式
def L(x, x_vals, y_vals):
    nearest_idxs = np.argpartition(np.abs(x_vals - x), 3)[:3]
    L_2 = 0
    for i in nearest_idxs:
        if i == nearest_idxs[0]:
            L_2 += y_vals[i] * ((x - x_vals[nearest_idxs[1]]) * (x - x_vals[nearest_idxs[2]])) / ((x_vals[i] - x_vals[nearest_idxs[1]]) * (x_vals[i] - x_vals[nearest_idxs[2]]))
        elif i == nearest_idxs[1]:
            L_2 += y_vals[i] * ((x - x_vals[nearest_idxs[0]]) * (x - x_vals[nearest_idxs[2]])) / ((x_vals[i] - x_vals[nearest_idxs[0]]) * (x_vals[i] - x_vals[nearest_idxs[2]]))
        elif i == nearest_idxs[2]:
            L_2 += y_vals[i] * ((x - x_vals[nearest_idxs[0]]) * (x - x_vals[nearest_idxs[1]])) / ((x_vals[i] - x_vals[nearest_idxs[0]]) * (x_vals[i] - x_vals[nearest_idxs[1]]))
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
x_vals_subset = np.linspace(0, 8, 100)
y_vals_subset = f(x_vals_subset)
x_interp = np.linspace(0, 8, 1000)
y_interp = [L(i, x_vals_subset, y_vals_subset) for i in x_interp]
y_true = f(x_interp)
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.plot(x_interp, y_true, label='真实函数',color='blue')
plt.scatter(x_vals_subset, y_vals_subset, label='数据点', s=5, color='red')
plt.legend()
plt.show()

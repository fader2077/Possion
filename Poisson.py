import math
import random
import numpy as np
import matplotlib.pyplot as plt


# 產生數據
def generate_data(lamba, num_samples):
    p = np.random.rand(num_samples)
    t = np.round(-1*np.log(1-p)/lamba, 6)
    return t
# 統計數據  
def count_data(t):
    counters = np.zeros(20000)
    for x in t:
        idx = int(x/0.00001)
        if idx < len(counters):
            counters[idx] += 1
    return counters

# 折線圖
def plot_results_plot(x, y,lamba):
    plt.plot(x, y)
    plt.xlabel('inter-arrival time x')
    plt.ylabel('approximate exponentials pdf(x) value')
    # plt.xlabel(f'inter-arrival time x = {max(x)}')
    # plt.ylabel(f'approximate exponentials pdf(x) value = {max(y)}')
    plt.title(f'Exponential Distribution Lamba = {lamba}')
    plt.show()
# 點狀圖
def plot_results_scatter(x, y,lamba):
    plt.scatter(x, y,s = lamba)
    plt.xlabel('inter-arrival time x')
    plt.ylabel('approximate exponentials pdf(x) value')
    # plt.xlabel(f'inter-arrival time x = {max(x)}')
    # plt.ylabel(f'approximate exponentials pdf(x) value = {max(y)}')
    plt.title(f'Exponential Distribution Lamba = {lamba}')
    plt.show()
# 柱狀圖
"""
def plot_results_bar(x, y,lamba):
    plt.bar(x, y)
    plt.xlabel('inter-arrival time x')
    plt.ylabel('approximate exponentials pdf(x) value')
    # plt.xlabel(f'inter-arrival time x = {max(x)}')
    # plt.ylabel(f'approximate exponentials pdf(x) value = {max(y)}')
    plt.title(f'Exponential Distribution Lamba = {lamba}')
    plt.show()
"""
if __name__ == '__main__':
    # num_samples = 1000000
    # lamba = 25 
    t = [] 
    lamba,num_samples = map(int,input().split())
    t = generate_data(lamba, num_samples)

    # 計數
    for i in range(num_samples):
        print(f'[{i}]:{t[i]}')
    print(f'The rate lambda is {lamba}')
    print(f'Average inter-arrival time is {np.mean(t)}')
    counters = count_data(t)
    # 實際指數分布
    x = np.arange(0, 0.3, 0.00003)
    y = counters[::2] + counters[1::2]
    plot_results_plot(x, y,lamba)
    plot_results_scatter(x, y,lamba)
    # plot_results_bar(x, y,lamba)
    # 近似指數分布
    y2 = lamba * np.exp(-lamba * x)
    plot_results_plot(x, y2,lamba)
    plot_results_scatter(x, y2,lamba)
    # plot_results_bar(x, y,lamba)
    # 檢驗具體function值
    print(f"p(0.02) = {(lamba * math.exp(-lamba * 0.02)):.3f}")
    print(f"p(0.04) = {(lamba * math.exp(-lamba * 0.04)):.3f}")
    print(f"p(0.1) = {(lamba * math.exp(-lamba * 0.1)):.3f}")
    print(f"p(0.2) = {(lamba * math.exp(-lamba * 0.2)):.3f}")
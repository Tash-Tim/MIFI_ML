import pandas as pd
import numpy as np

# Hut_Paradise_DF = pd.DataFrame({
#     '1.Rent': [65, 70, 120, 35, 40, 50, 100, 90, 85],
#     '2.Area': [50, 52, 80, 33, 33, 44, 80, 65, 65],
#     '3.Rooms':[3, 2, 1, 1, 1, 2, 4, 3, 2],
#     '4.Floor':[5, 12, 10, 3, 6, 13, 8, 21, 5],
#     '5.Demo two weeks':[8, 4, 5, 10, 20, 12, 5, 1, 10],
#     '6.Liv.Area': [37, 40, 65, 20, 16, 35, 60, 50, 40]
# })
#print(Hut_Paradise_DF) # получили матрицу из словаря

# demo_time = np.array([10, 20, 30, 15, 5, 40, 20, 8, 20])
# print(demo_time)

# Hut_Paradise_values = Hut_Paradise_DF.values #из словаря вытащили список (матрицу значений)
# print(Hut_Paradise_values[4]) # выводим строку(вектора) матрицы по номеру
# print(Hut_Paradise_values[:,3]) # выводим столбца(вектора) матрицы по номеру
# print(Hut_Paradise_values[:,3][5]) # выводим элемент столбца (вектора) по номеру
# print(len(Hut_Paradise_values[:,3])) # размерность столбца (вектора)
# print(Hut_Paradise_values[:,1] - Hut_Paradise_values[:,5])

# demo_two_week = Hut_Paradise_values[:,4]
# print(demo_two_week)

# demo_time_two_week = demo_time * demo_two_week # поэлементное умножение векторов
# print(sum(demo_time_two_week))

# u=np.array([3,0,1,1,1])
# v=np.array([0,1,0,2,-2])
# w=np.array([1,-4,-1,0,-2])
#
# lin_comb = 2 * v + (-3)*w
# print(lin_comb)
#
# resulr = np.dot(u, lin_comb)
# print(resulr)

x = np.array([1, 2, 3])
y = np.matrix([1, 2, 3])
print(x, x.shape, type(x),'\n', np.reshape(x, (3,1)),'\n')
print(y, y.shape, type(y),'\n', np.reshape(y, (3, 1)),'\n')


print()
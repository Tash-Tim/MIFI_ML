import numpy as np
import pandas as pd

# A = np.array([[5,-1,3,1,2], [-2,8,5,-1,1]])
# x = np.array([1,2,3,4,5])
# print(A)
# print(x)
#
# Ax = np.dot(A, x)
# print(Ax)
# xA = np.dot(x, A)
# print(xA)

# A = np.array([[1,9,8,5], [3,6,3,2], [3,3,3,3], [0,2,5,9], [4,4,1,2]])
# B = np.array([[1,-1,0,1,1], [-2,0,2,-1,1]])
# try:
#     print(np.dot(A, B))
# except ValueError:
#     print('1-st no')
#     print(np.dot(B,A))
# except ValueError:
#     print('2-nd no')

# x = np.array([1,2,1,0,4])
# y = np.array([2,1,-1,1,0])
# z = np.array([-1,1,-1,0,0])
#
# A = np.array([x, y, z])
#
# print(np.dot(A,A.T), '\n')
# print(np.dot(A.T,A))

Count_DF = pd.DataFrame({
    'Женские стрижки': [10, 2, 12, 4, 6, 10, 22, 7],
    'Мужские стрижки': [5, 21, 12, 8, 25, 3, 1, 0],
    'Окрашивания':[12, 3, 0, 18, 27, 2, 4, 31],
    'Укладка':[15, 25, 30, 14, 25, 17, 25, 31],
    'Уход':[10, 6, 4, 5, 18, 12, 20, 28]
    },
    index=['Аня', 'Борис', 'Вика', 'Галя', 'Дима', 'Егор', 'Женя','Юра']
)
Price_DF = pd.DataFrame({
    'Женские стрижки': [2, 1.8, 2, 1.8, 2.5, 5, 1.1, 4.5],
    'Мужские стрижки': [1.5, 2.5, 2, 1.2, 3.5, 5, 1, 4],
    'Окрашивания':[1, 1, 0, 2.8, 2, 3, 1.5, 2.5],
    'Укладка':[0.8, 1, 0.5, 0.8, 1, 2, 0.5, 1],
    'Уход':[1, 1, 2, 2, 1.5, 2.5, 1.7, 2]
    },
    index=['Аня', 'Борис', 'Вика', 'Галя', 'Дима', 'Егор', 'Женя','Юра']
)
print('Количество услуг: \n', Count_DF)
print('Стоимость услуг: \n', Price_DF)

Count_DF_val = Count_DF.values
Price_DF_val = Price_DF.values
print('\n', Count_DF_val)
print(Price_DF_val, '\n')

stil_tot_price = Count_DF_val * Price_DF_val
print(stil_tot_price, '\n')

com = np.array([0.2, 0.2, 0.3, 0.1, 0.1])
saloon_price = stil_tot_price @ com
print(saloon_price)

one_vec = np.array([1, 1 ,1 ,1 ,1 ])
stil_tot_price_vec = stil_tot_price @ one_vec
print(stil_tot_price_vec - saloon_price)
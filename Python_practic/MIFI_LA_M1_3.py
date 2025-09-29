import numpy as np

Husband_Income = np.array([100,220,140])
Wife_Income = np.array([150,200,130])
Mother_In_Law_Income = np.array([90,80,100])

Husband_Consumption = np.array([50,50,60])
Wife_Consumption = np.array([100,80,140])
Mother_In_Law_Consumption = np.array([100,20,140])

incom_matrix = np.array([Husband_Income, Wife_Income, Mother_In_Law_Income]).T
print(incom_matrix, '\n')

cons_matrix = np.array([Husband_Consumption, Wife_Consumption, Mother_In_Law_Consumption]).T
print(cons_matrix, '\n')

coms_1_month = incom_matrix[0]
print(coms_1_month)
after_tax = coms_1_month - 0.13 * coms_1_month
print(after_tax, '\n')

balans_3_month = (incom_matrix[2] - 0.13 * incom_matrix[2]) - cons_matrix[2]
print(balans_3_month)
import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_num = int(input('Угадай число от 1 до 100: '))
    
    if predict_num > number:
        print("Число должно быть меньше!")

    elif predict_num < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break
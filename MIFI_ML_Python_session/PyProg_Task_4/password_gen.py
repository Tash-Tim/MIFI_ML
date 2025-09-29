import random
import string

def pas_gen(pas_length :int) -> str:
    all_sym = string.ascii_letters + string.digits + string.punctuation
    # вместо библиотеки string можно вручную составить текст состоящий из всех цифр, букв и символов

    frst_sym = random.choice(string.ascii_letters + string.digits)
    res_sym = ''.join([random.choice(all_sym) for _ in range(pas_length - 1)])

    result = frst_sym + res_sym
    return result


user_length = int(input('Введите длину пароля: '))
generated = pas_gen(user_length)
print('Пароль сгенерирован:', generated)



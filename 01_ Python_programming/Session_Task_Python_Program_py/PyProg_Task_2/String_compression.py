def str_comres(get_str):
    result = ''
    sym_cnt = {i_unq:get_str.count(i_unq) for i_unq in get_str}
    for i_sym, i_cnt in sym_cnt.items():
        if i_cnt > 1:
            result += i_sym + str(i_cnt)
        else:
            result += i_sym

    return result


#user_str = input('Введите строку: ')
user_str = 'affbfghaaa'
print(f'Исходный текст: {user_str}')
print('Сжатая строка:', str_comres(user_str))
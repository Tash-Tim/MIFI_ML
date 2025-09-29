def str_comres(get_str):
    result = ''
    def uniq_sym_fun():
        nonlocal get_str
        uniq_sym = []
        for i_sym in get_str:
            if i_sym not in uniq_sym:
                uniq_sym.append(i_sym)
        return uniq_sym

    sym_cnt = {i_unq:get_str.count(i_unq) for i_unq in uniq_sym_fun()}
    for i_sym, i_cnt in sym_cnt.items():
        if i_cnt > 1:
            result += i_sym + str(i_cnt)
        else:
            result += i_sym

    return result


user_str = input('Введите строку: ')
print('Сжатая строка:', str_comres(user_str))
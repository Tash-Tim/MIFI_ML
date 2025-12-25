from math import ceil

def shredinder_fun(text, percent):
    # считаем кол-во знаков пунктуации в текста
    punct_lst = [i_punct for i_punct in list(text) if not i_punct.isalpha() and i_punct != ' ']
    # рассчитываем общее количество элементов для замены во всей строке
    tot_del_elem = ceil(len(text.split()) * (percent / 100))

    result = ''
    temp_text_cnt = 0
    temp_text = ''

    for i_text in text:
        # формируем временный текст до первого знака пунктуации и считаем количество элементов
        if i_text not in punct_lst:
            temp_text += i_text
            temp_text_cnt = len(temp_text.split())
        else:
            # рассчитываем кол-во элементов для замены во временном тексте
            temp_del_elem = temp_text_cnt / len(text.split()) * tot_del_elem
            # рассчитываем начальную позицию для замены (конечная позиция = temp_del_elem)
            start_del_elem = (temp_text_cnt / 2) - (temp_del_elem / 2)
            temp_text_lst = temp_text.split()
            temp_text_lst[ceil(start_del_elem) : ceil(start_del_elem + temp_del_elem)] = ['...']

            result += ' '.join(temp_text_lst)
            temp_text = ''
            temp_text_cnt = 0

    return result


user_text = input('Введите текст для обработки: ')
user_perc = int(input('Введите процент обработки текста: '))

print(shredinder_fun(user_text, user_perc))
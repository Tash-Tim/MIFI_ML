def bracket_check(text: str):
    open_brack = {'(', '[', '{'}
    close_brack = {')': '(', ']': '[', '}': '{'}
    open_brack_lst = []

    for i_text in text:
        if i_text in open_brack:
            # добавляем открытые скобки в open_brack_lst
            open_brack_lst.append(i_text)
        elif i_text in close_brack:
            # проверяем закрытые скобки с последними, добавленными открытыми скобками в open_brack_lst
            if not open_brack_lst or open_brack_lst[-1] != close_brack[i_text]:
                return False
            # в случае совпадения открытых и закрытых скобок, удаляем последние открытые скобки из open_brack_lst
            open_brack_lst.pop()
# если open_brack_lst НЕ пуст значит расстановка скобок некорректна
    return not open_brack_lst

user_text = input('Веедите текст со скобками: ')
print(bracket_check(user_text))
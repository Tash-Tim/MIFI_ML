def about_palin_fun(text: str):

    def text_modif_fun(get_text):
         for i_index in range(len(get_text)):
            mod_text = get_text[: i_index] + get_text[i_index + 1:]
            if mod_text == mod_text[::-1]:
                return f'Текст {get_text} - палиндром, если удалить {get_text[i_index]}'
         else:
            return f'Текст {get_text} - НЕ может быть палиндромом'

    if text == text[::-1]:
        return f'Текст {text} - палиндром'
    else:
        return text_modif_fun(text)


user_text = input('Введите текст: ')
print(about_palin_fun(user_text))
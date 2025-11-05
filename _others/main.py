# import numpy as np
# a = [1, 2]
# user_lst = [-3, 1]
# c = [1, 2]
# d = [1, -1]
#
# A = np.array([a,user_lst,c,d])
# print(A, '\n')
#
# G = A.T @ A
# print(G, '\n')
#
# inv = np.linalg.inv(G)
# print(inv)
#
# b_vec = np.array([1, 4, 5, 0])
# print(b_vec)
#
# AT_b = A.T @ b_vec
# print(AT_b)
#
# w = inv @ AT_b
# print(w)

# data = {"v" : [5, 1, 2], 'u' : [4, 2, 8]}
# VU = pd.DataFrame(data, index=('a', 'user_lst', 'c'))
# print(VU)
# forf = VU.corr()
# print(forf)

# print(v, u)
#
# #___________________________________________________
# v_mid = round(sum(v)/len(v), 2)
# u_min = round(sum(u)/len(u), 2)
# print(v_mid, u_min)
#
# v_cent = v - v_mid
# u_cent = u - u_min
# print(v_cent, u_cent)
#
# vu_cent_mult = round(v_cent @ u_cent, 2)
# print(vu_cent_mult)
#
# #__________________________________________________-
# v_cent_norm = np.linalg.norm(v_cent)
# u_cent_norm = np.linalg.norm(u_cent)
# print(v_cent_norm, u_cent_norm)
#
# vu_norm_mult = v_cent_norm * u_cent_norm
# print(vu_norm_mult)
#
# korr_koef = round(vu_cent_mult / vu_norm_mult, 2)
# print(korr_koef)
# a = [[1, 1, 1, 1, 1], [1, 0, -3, 2, 4], [2, 0, -6, 4, 8]]
# y = [4, 6, -4, 2, 7]
#
# A = np.array(a).T
# Y = np.reshape(y, [5, 1])
#
# print(A)
# print(Y)
#
# A_Gram = A.T@A
# print(A_Gram)
#
# A_det = np.linalg.det(A_Gram)
# print(A_det)
#
# A_Gram_ridge = A_Gram + 5
# A_ridge_det = np.linalg.det(A_Gram_ridge)
# print('\n', A_Gram_ridge)
# print(A_ridge_det)
#_______________________________________________
# import cmath
# x = cmath.sqrt(-1)
# print(x)
#________________________________________________
# reg = [('Ivanov', 'Sergej', 24, 9, 1995),
#       ('Smith', 'John', 13, 2, 2003),
#       ('Petrova', 'Maria', 13, 3, 2003)]
# filter_fum = filter(lambda x: x[4]>2000, reg)
# new_reg = map(lambda y: (y[0]+' '+y[1][0]+'.', *y[3:]), filter_fum)
#
# print(list(new_reg))
#_____________________________________________________________________

# a = [[3, -3, -5, 8], [-3, 2, 4, -6], [2, -5, -7, 5], [-4, 3, 5, -6]]
# A = np.array(a)
# A_det = np.linalg.det(A)
# print(A)
# print(A_det)


'''
Напишите функцию holes_count(), которая принимает на вход число number, подсчитывает общее количество отверстий в 
заданном числе и возвращает результат.
Условимся, что цифрами с отверстиями будем считать 0, 4, 6, 8 и 9. Причём в цифре 8 отверстий два, а в остальных —
по одному.
Обратите внимание, что функция должна возвращать суммарное количество отверстий по всем цифрам в числе.
'''
# def holes_count(number):
#     str_number = str(number)
#     holes_dict = {"0": 1, "4": 1, "6": 1, "8": 2, "9": 1}
#     holes_count = sum(map(lambda x: holes_dict.get(x, 0), str_number))
#     return holes_count

# def print_personal_data(**data):
#     sort_data = sorted(data, key=lambda get_key: get_key[0])
#     for i_data in sort_data:
#         print(f'{i_data}: {data[i_data]}')
#
# print_personal_data(first_name='John', last_name='Doe', age=28, position='Python developer')

# def get_words_list(text):
#     punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
#     text = text.lower()
#     for symbol in punctuation_list:
#         text = text.replace(symbol, '')
#     return text.split()
#
# text_example = "Arrakis, the planet known as Dune, is forever his place."
# print(get_words_list(text=text_example))
#__________________________________________________________________________________________
# def get_most_frequent_word(text):
#
#     def get_words_list(text):
#         punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
#         text = text.lower()
#         for symbol in punctuation_list:
#             text = text.replace(symbol, '')
#         word_lst = text.split()
#         return word_lst
#
#     def get_unique_words(words_list=None):
#         if words_list is None:
#             words_list = list()
#         result = list(set(words_list))
#         result.sort()
#         return result
#
#     clear_text = get_words_list(text)
#     uniq_word = get_unique_words(clear_text)
#
#
#     def max_word_count(clear_text, uniq_word):
#         max_cnt = 0
#         max_word = ''
#         for i_word in uniq_word:
#             if max_cnt < clear_text.count(i_word):
#                 max_cnt = clear_text.count(i_word)
#                 max_word = i_word
#         return max_word
#
#     return max_word_count(clear_text, uniq_word)
#
#
# text_example = ("A beginning is the time for taking the most delicate care that the balances are correct. This every  "
#                 "sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that "
#                 " you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And "
#                 "take  the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be  "
#                 "deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis,  "
#                 "the planet known as Dune, is forever his place.")
# print(get_most_frequent_word(text_example)a

# data = [
#     ('Amanda', 37, 78, 67),
#     ('Patricia', 78, 93, 68),
#     ('Marcos', 79, 67, 89),
#     ('Dmitry', 67, 68, 100),
#     ('Andrey', 100, 78, 76),
#     ('Victoria', 93, 69, 96),
# ]
#
# add_tot = lambda data_tuple: (*data_tuple, sum(data_tuple[1:]))
# map_data = map(add_tot, data)
# sorted_map = sorted(map_data, key=lambda map_data_tot: map_data_tot[4], reverse=True)
#
# print(sorted_map)

# def count_money(cheese_data):
#     tot_cnt = map(lambda price_cnt: price_cnt[0]*(price_cnt[1] * 1000 // 100), cheese_data.values())
#     return sum(tot_cnt)
#
#
# def find_cheese_type(cheese_data=None, cheese_type=None):
#     if cheese_data is None:
#         cheese_data = dict()
#
#     # type_filter_fun = lambda type_name: type_name[1][-1] == cheese_type
#     # type_filer = filter(type_filter_fun, cheese_data.items())
#     # cheese_lst = map(lambda type_lst: type_lst[0], type_filer)
#
#     cheese_lst = [i_name for i_name, i_data in cheese_data.items() if i_data[-1] == cheese_type]
#
#     return cheese_lst
#
#
# def sort_cheese(cheese_data=None):
#     if cheese_data is None:
#         cheese_data = list()
#
#     chees_sort = sorted(cheese_data.items(), key=lambda chees_detail: chees_detail[1][0])
#     cheese_sort_lst = list(map(lambda cheese_name: cheese_name[0], chees_sort))
#     return cheese_sort_lst
#
#
# cheese_data = {
#     'чеддер': [370, 5000, 33, 'твердый'],
#     'пармезан': [510, 4000, 29, 'твердый'],
#     'гауда': [250, 3700, 27, 'полутвердый'],
#     'эдам': [220, 10000, 30, 'полутвердый'],
#     'горгонзола': [320, 3000, 32, 'полумягкий'],
#     'рокфор': [340, 15000, 31, 'полумягкий'],
#     'стилтон': [360, 7000, 35, 'полумягкий'],
#     'камамбер': [250, 8000, 24, 'мягкий'],
#     'бри': [310, 6500, 28, 'мягкий'],
# }


# def purchase(ingredients=None):
#     if ingredients is None:
#         ingredients = list()
#
#     def uniq_fun(non_uniq_lst):
#         uniq_ingrid = list()
#         for i_elem in non_uniq_lst:
#             if i_elem not in uniq_ingrid:
#                 uniq_ingrid.append(i_elem)
#         return uniq_ingrid
#
#     if len(ingredients) == len(set(ingredients)):
#         print('Ваш заказ оформлен верно')
#     else:
#         for i_ingrid in uniq_fun(ingredients):
#             ingrid_count = ingredients.count(i_ingrid)
#             if ingrid_count > 1:
#                 print(f'Вы продублировали ингредиент {i_ingrid} в заказе {ingrid_count} раз(а)')
#
#
# ingredients = ['молоко коровье', 'молоко овечье', 'бактерии', 'молоко козье', 'сливки', 'фермент', 'закваска',
#                'молоко  коровье', 'соль', 'молоко коровье', 'бактерии', 'молоко овечье', 'кислота лимонная',
#                'грибки',  'соль', 'дрожжи', 'кислота уксусная', 'кальций', 'калий', 'каротин', 'аннато', 'специя',
#                'пряность', 'ароматизатор', 'соль', 'кислота молочная']
#
# purchase(ingredients)

import numpy as np

A= np.array([[3, 51], [1, 30], [2, 45]], )
print(A)
print()
AT = A.T
print(AT)
print()
x = np.dot(AT,A)
print(x)
print()
x_rev= np.linalg.inv(x)
print(x_rev)
print()
e = x@x_rev
print(e)
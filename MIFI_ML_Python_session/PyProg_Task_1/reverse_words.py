with open('word_file.txt', 'r', encoding='utf8') as from_file:
    read_file = from_file.readlines()
    print(f'Исходный текст:\n', *read_file)

# так как переворот происходит независимо от места в блоке, то сначала переворачивает предложение по отдельности
    rev_sent = [' '.join(reversed(i_sent.split())) for i_sent in read_file]
# Формируем блок из нескольких предложений. Я решил разделить их попарно: к каждому предложению добавить следующее
# предложение
    blocks = [", ".join((rev_sent[i], rev_sent[(i+1) % len(rev_sent)])) for i in range(len(rev_sent))]
    print(f'\nТекст после обработки:\n {'\n '.join(blocks)}')
"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open('file_for_task_2.txt', encoding='utf-8') as file:
    for idx, el in enumerate(file, start=1):
        word = el[:-1]
        split_el = word.split(' ')
        quantity_words = len(split_el)
        print(f'Строка: {idx}. Количество слов: {quantity_words}')

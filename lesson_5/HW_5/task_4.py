"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from googletrans import Translator

translator = Translator()

with open('file_for_task_4_ru.txt', 'a+', encoding='utf-8') as file_ru:
    with open('file_for_task_4.txt', encoding='utf-8') as file:
        for data_str in file:
            data_str_ru = translator.translate(data_str, dest='ru')
            file_ru.write(data_str_ru.text + '\n')

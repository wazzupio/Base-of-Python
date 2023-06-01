"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

numbers = '1 2 3 4 5'

with open('file_for_task_5.txt', 'a+', encoding='utf-8') as file:
    numbers_split = numbers.split()
    numbers_sum = sum(list(map(int, numbers_split)))
    file.write(f'Cумма чисел {numbers} равна: {numbers_sum}')

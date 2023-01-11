"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
my_dict = {}
lessons_names = []
lessons_hours = []

with open('file_for_task_6.txt', encoding='utf-8') as file:
    for data_str in file:
        data_list = data_str.split()
        lesson = data_list.pop(0)
        lessons_names.append(lesson[:-1])

        for idx, el in enumerate(data_list):
            if el == '—':
                data_list[idx] = '0'
                continue
            idx_bracket = el.find('(')
            data_list[idx] = el[:idx_bracket]

        sum_hours = sum(list(map(int, data_list)))
        lessons_hours.append(sum_hours)

for i in range(len(lessons_names)):
    my_dict[lessons_names[i]] = lessons_hours[i]

print(my_dict)

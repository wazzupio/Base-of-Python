"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('file_for_task_3.txt', encoding='utf-8') as file:
    workers_names = []  # Cписок имен всех сотрудников
    workers_salaries = []  # Cписок зарплат всех сотрудников
    names = []  # Cписок имен сотрудников у которых меньше 20 тыс.
    salaries = []  # Cписок зарплат сотрудников у которых меньше 20 тыс.

    for data_str in file:
        name_worker = data_str.split(' ')[0]
        salary_worker = int(data_str.split(' ')[1])

        workers_names.append(name_worker)
        workers_salaries.append(salary_worker)

        if salary_worker < 20000:
            names.append(name_worker)
            salaries.append(salary_worker)

    average_salaries = sum(workers_salaries) / len(workers_names)

print(f'Список сотрудников у которых оклад менее 20 тыс:', ', '.join(names))
print(f'Средняя величина дохода сотрудников: {average_salaries}')

"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

all_names_with_profit = []
all_profits = []

all_names_with_loss = []
all_loss = []

with open('file_for_task_7.txt', encoding='utf-8') as file:
    for data_str in file:
        data_list = data_str.split()
        firm_profit = int(data_list[-2]) - int(data_list[-1])

        if firm_profit > 0:
            all_names_with_profit.append(data_list[0])
            all_profits.append(firm_profit)
        else:
            all_names_with_loss.append(data_list[0])
            all_loss.append(firm_profit)

print(all_names_with_profit, all_profits)
print(all_names_with_loss, all_loss)

average_profit = round(sum(all_profits) / len(all_profits), 2)

dict_name_profit = {}
dict_name_loss = {}
dict_average = {'average_profit': average_profit}

for i in range(len(all_names_with_profit)):
    dict_name_profit[all_names_with_profit[i]] = all_profits[i]

for el in range(len(all_names_with_loss)):
    dict_name_loss[all_names_with_loss[el]] = all_loss[el]

result = {'data': {'companies_with_profit': dict_name_profit, 'average': dict_average,
                   'companies_with_loss': dict_name_loss}}

with open('json_for_task_7.json', 'w+', encoding='utf-8') as file_json:
    json.dump(result, file_json)

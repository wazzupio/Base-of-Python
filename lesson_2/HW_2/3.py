"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

#  Решение задачи через list

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

seasons = [winter, spring, summer, autumn]
seasons_ru = ['Зима', 'Весна', 'Лето', 'Осень']

month_user = int(input("Введите месяц в виде целого числа от 1 до 12: "))

for season in seasons:
    if month_user in season:
        idx = seasons.index(season)
        print(f"Месяц под номером {month_user} это {seasons_ru[idx]}")

#  Решение задачи через dict

# seasons = {
#     'Зима': [12, 1, 2],
#     'Весна': [3, 4, 5],
#     'Лето': [6, 7, 8],
#     'Осень': [9, 10, 11],
# }
#
# month_user = int(input("Введите месяц в виде целого числа от 1 до 12: "))
#
# for season in seasons.items():
#     if month_user in season[1]:
#         print(f"Месяц под номером {month_user} это {season[0]}")

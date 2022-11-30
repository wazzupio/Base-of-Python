"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

user_sec = int(input("Введите время в секундах:"))

hours = user_sec // 3600
minutes_all = user_sec // 60
minutes = minutes_all % 60
seconds = user_sec % 60

print(f"{user_sec} секунд - {hours}:{minutes}:{seconds}")

"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(first_name, surname, year_of_birth, city, email=None, phone=None):
    print(f'Имя: {first_name}, Фамилия: {surname}, Год рождения: {year_of_birth}, Город проживания: {city},'
          f' email: {email}, Телефон: {phone}')


user_data(first_name='Василий', surname='Пупкин', year_of_birth='1980', city='Москва', phone=8999)

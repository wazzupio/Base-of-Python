"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
сумме и после этого завершить программу.
"""


def sum_before_q(list_str):
    els_before_q = []
    for el in list_str:
        if el == "q":
            sum_els = sum(map(int, els_before_q))
            return sum_els
        else:
            els_before_q.append(el)


user_str = input("Введите несколько чисел через пробел\nДля выхода из программы введите 'q': ").split()

total_sum = 0

while True:
    if user_str == "q":
        print(f"Сумма чисел: {total_sum}")
        break
    if "q" in user_str:
        total_sum = sum_before_q(user_str) + total_sum
        print(f"Сумма чисел: {total_sum}")
        break

    sum_user_str = sum(list(map(int, user_str)))
    total_sum += sum_user_str

    print(f"Сумма чисел: {total_sum}")
    user_str = input("Введите еще несколько чисел через пробел: ").split()

"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
# Решение через sys.argv
from sys import argv
from argparse import ArgumentParser

# script_name, work_time_in_hours, earning_per_hour, bonus = argv
# wage = (int(work_time_in_hours) * int(earning_per_hour)) + int(bonus)
#
# print(f'Заработная плата сотрудника: {wage}')

# Решение через argparse.ArgumentParser

parser = ArgumentParser()

parser.add_argument('--time', type=int)
parser.add_argument('--earning', type=int)
parser.add_argument('--bonus', type=int)

args = parser.parse_args()
wage = (args.time * args.earning) + args.bonus

print(f'Заработная плата сотрудника: {wage}')

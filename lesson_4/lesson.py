"""arg parser"""

# from sys import argv
# from argparse import ArgumentParser
#
# parser = ArgumentParser()
#
# parser.add_argument('--name', type=str)
# parser.add_argument('--age', type=int)
# parser.add_argument('--place', type=str, default='Shop')
#
# args = parser.parse_args()
#
# print(f'In our args {args}.\nType {type(args)}')
# print(f'Hello, {args.name}! You are {args.age}. You work in {args.place}')

# script_name, name, surname = argv
#
# print(f'Our args is {argv}. It is type {type(argv)}, {type(argv[0])}')
# print(f'Hello, worker {name}, {surname}')
import time

"""import and import from time, random, os"""
# import time
# import os
# import random

# for i in range(5):
#     print(f'Hello. It is {i}')
#     time.sleep(5)

# files = os.listdir()
# path = os.getcwd()
#
# print(files)
# print(path)

# ids = [12, 17, 16, 90]
#
# print(random.randint(0, 20))
# print(random.sample(ids, 2))

"""генераторы"""

# random_str = ['cat', 'dog', '3', 'mouse', '1']
# new_random_list = []
#
# for el in random_str:
#     new_random_list.append(el.title())
#
# # print(new_random_list)
#
# better_new_random_list = (el.title() for el in random_str if not el.isdigit())
# print(better_new_random_list)
# print([el for el in better_new_random_list])
# print([el for el in better_new_random_list])

"""yield"""


# def my_gen(num):
#     for i in range(num):
#         yield i
#
#
# x = my_gen(5)
#
# print(x)
# print([el for el in x])
# print([el for el in x])

"""functools and itertools"""

# from functools import reduce


# def my_f(symbol_1, symbol_2):
#     return symbol_1 + symbol_2
#
#
# random_str = ['a', 'b', 'c', 'd', 'e']
# print(reduce(my_f, random_str))

from itertools import count, cycle

# for el in count(10, 20):
#     print(el)
#     time.sleep(1)
#     if el >= 50:
#         break

random_str = ['a', 'b', 'c', 'd', 'e']   # first in first out FIFO
iter_str = cycle(random_str)

print(next(iter_str))
print(next(iter_str))
print(next(iter_str))

"""math"""
# import math
#
# print(math.sqrt(math.pi))

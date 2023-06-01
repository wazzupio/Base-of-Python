# f = open('for_lesson_5.txt', 'w')
# data_for_file = ['Milk\n', 'Bread\n', 'Sugar\n']
# f.writelines(data_for_file)
# f.close()
#
# f = open('for_lesson_5.txt')
# data = f.readlines()
# print(type(data))
# print(data)
# f.close()

"""Менеджеры контекста"""
# try:
#     print('Try to open')
#     f = open('for_lesson_5.txt')
# except:
#     print('Fail')
#     print('No!')
# finally:
#     f.close()
#     print('Closed!')

# with open('for_lesson_5.txt', 'a') as f:
#     f.writelines(['Potato\n', 'Egg\n'])
#
# with open('for_lesson_5.txt', 'r') as f:
#     for line in f:
#         print(line)

"""pandas"""
# import pandas as pd
#
# data = pd.read_csv('train.csv')
# print(data['Survived'])

"""json"""
# import json
#
# worker = {"age": 27, "name": "Basil", "vaccine": 1}
# # with open('notebook_1.json', 'w') as f:
# #     json.dump(worker, f)
#
# with open('notebook_1.json') as f:
#     data = json.load(f)
#
# print(data)

import os
import shutil

# os.makedirs('Test1', exist_ok=True)
# os.makedirs('Test1/Test_2', exist_ok=True)
# os.makedirs('Data', exist_ok=True)
# files = os.listdir()
#
# for file in files:
#     print(file)
#
# shutil.move('for_lesson_5.txt', 'Data')

"""Определение позиции """

# with open("for_lesson_5.txt", "r+") as f:
#     print("Init position:", f.tell())
#     data = f.read()
#     print("Mid position:", f.tell())
#     print(data)
#
#     f.write('File was visited time!')
#     data_new = f.read()
#     print("I am new!", data_new)
#     print("Last position:", f.tell())

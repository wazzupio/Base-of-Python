""" classmethod and staticmethod """


# class Form:
#     ids = []
#     default_id = 0
#     class_name = 'Form'
#     """
#     Возможные варианты даты:
#     21 августа 1996
#     21.08.96
#     08.21.96
#     """
#     def __init__(self, name, birth, id=None):
#         self.name = name
#         self.birth = birth
#         if id is not None and id not in Form.ids:
#             self.id = id
#         else:
#             while Form.default_id in Form.ids:
#                 Form.default_id += 1
#             self.id = Form.default_id
#         Form.ids.append(self.id)
#
#     @staticmethod
#     def form_birth(birth):
#         name = 'John Doe'
#         birth = birth
#         return Form(name, birth)
#
#     def __str__(self):
#         return f'{self.name}, {self.birth}, {self.id}'
#
#     @staticmethod
#     def print_hello_static():
#         print('Hello! static')
#
#     @classmethod
#     def print_hello_class_method(cls, birth):
#         return cls.form_birth(birth)
#
#
# class BigForm(Form):
#     class_name = 'BigForm'
#
#
# user_1 = Form('Basil', '21.08.1996', 4242)
# user_2 = Form.form_birth('19.09.1996')
# user_3 = Form.form_birth('19.09.1991')
#
# print(user_1)
# print(user_2)
# print(user_3)
#
# print(Form.print_hello_class_method('xz.Form.1993'))
# print(BigForm.print_hello_class_method('xz.BigForm.1994'))

""" requests """
# import requests
#
# req = requests.get('https://gb.ru')
#
# print(req.encoding)
#
# with open('gb.html', 'wb') as file:
#     for chunk in req.iter_content(chunk_size=50000):
#         file.write(chunk)


""" try except """

try:
    print(5 / 0)
except ZeroDivisionError:
    print('0 NO !!!')
else:
    print('Else')
finally:
    print('Finally')

test = []
for i in range(6):
    test.append(i)
    print('Hello', i)
else:
    test.append('!')
    print('End it all')

print(test)

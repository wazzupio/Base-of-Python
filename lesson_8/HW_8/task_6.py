"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Stock:
    printers_with_colors = []
    printers_without_colors = []
    scanners_with_bluetooth = []
    scanners_without_bluetooth = []
    faxes_with_timer = []
    faxes_without_timer = []

    def __init__(self, name_stock, address, email):
        self.name_stock = name_stock
        self.address = address
        self.email = email

    def __str__(self):
        return f'----------\nНазвание склада: {self.name_stock}, Адресс: {self.address},' \
               f' Email: {self.email}\n----------'

    @classmethod
    def info(cls, self):
        return f'----------\nСклад: "{self.name_stock}"\nЦветной принтер: {cls.printers_with_colors} шт\n' \
               f'Черно-белый принтер: {cls.printers_without_colors} шт\n' \
               f'Сканер с bluetooth: {cls.scanners_with_bluetooth} шт\n' \
               f'Сканер без bluetooth: {cls.scanners_without_bluetooth} шт\n' \
               f'Факс с таймером: {cls.faxes_with_timer} шт\n' \
               f'Факс без таймера: {cls.faxes_without_timer} шт\n----------'


class OfficeEquipment:
    def __init__(self, name_model, price, quantity):
        self.name_model = name_model
        self.quantity = quantity
        try:
            if price.isdigit():
                self.price = price
            else:
                raise AttributeError
        except AttributeError:
            print(f"Введено не число!!!")


class Printer(OfficeEquipment):
    def __init__(self, name_model, price, quantity, with_colors):
        super().__init__(name_model, price, quantity)
        self.with_color = with_colors

    def __str__(self):
        return f'{Printer.__name__} - Название модели: {self.name_model}, Цена: {self.price},' \
               f' Кол-во: {self.quantity}, Цветной: {self.with_color}'

    def send_to_stock(self):
        printer_dict = {'Название модели': self.name_model, 'Цена': self.price,
                        'Кол-во': self.quantity}
        if self.with_color is True:
            Stock.printers_with_colors.append(printer_dict)
        else:
            Stock.printers_without_colors.append(printer_dict)


class Scanner(OfficeEquipment):

    def __init__(self, name_model, price, quantity, with_bluetooth):
        super().__init__(name_model, price, quantity)
        self.with_bluetooth = with_bluetooth

    def __str__(self):
        return f'{Scanner.__name__} - Название модели: {self.name_model}, Цена: {self.price},' \
               f' Кол-во: {self.quantity}, Bluetooth: {self.with_bluetooth}'

    def send_to_stock(self):
        scanner_dict = {'Название модели': self.name_model, 'Цена': self.price,
                        'Кол-во': self.quantity}
        if self.with_bluetooth is True:
            Stock.scanners_with_bluetooth.append(scanner_dict)
        else:
            Stock.scanners_without_bluetooth.append(scanner_dict)


class Fax(OfficeEquipment):
    def __init__(self, name_model, price, quantity, with_timer):
        super().__init__(name_model, price, quantity)
        self.with_timer = with_timer

    def __str__(self):
        return f'{Fax.__name__} - Название модели: {self.name_model}, Цена: {self.price},' \
               f' Кол-во: {self.quantity}, Таймер: {self.with_timer}'

    def send_to_stock(self):
        fax_dict = {'Название модели': self.name_model, 'Цена': self.price, 'Кол-во': self.quantity}
        if self.with_timer is True:
            Stock.faxes_with_timer.append(fax_dict)
        else:
            Stock.faxes_without_timer.append(fax_dict)


stock_1 = Stock('Склад оргтехники', 'ул.Гагарина, д.10', 'stock@mgail.moc')

printer_1 = Printer('xerox', '15000', '6', True)
printer_2 = Printer('sony', '12000', '3', True)
printer_3 = Printer('hp', '9000', '10', False)
scanner_1 = Scanner('canon', '90000', '5', False)
fax_1 = Fax('samsung', '200000', '3', True)
fax_2 = Fax('samsung', '15000', '1', False)

print(stock_1)

printer_1.send_to_stock()
printer_2.send_to_stock()
printer_3.send_to_stock()
scanner_1.send_to_stock()
fax_1.send_to_stock()
fax_2.send_to_stock()

print(printer_1)
print(scanner_1)
print(fax_1)
print(Stock.info(stock_1))


"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Stock:
    quantity_printers_with_colors = 0
    quantity_printers_without_colors = 0
    quantity_scanners_with_bluetooth = 0
    quantity_scanners_without_bluetooth = 0
    quantity_faxes_with_timer = 0
    quantity_faxes_without_timer = 0

    def __init__(self, name_stock, address, email):
        self.name_stock = name_stock
        self.address = address
        self.email = email

    def __str__(self):
        return f'Название склада: {self.name_stock}, Адресс: {self.address},' \
               f' Email: {self.email}'

    @classmethod
    def info(cls, self):
        return f'Склад: "{self.name_stock}"\nЦветной принтер: {cls.quantity_printers_with_colors} шт\n' \
               f'Черно-белый принтер: {cls.quantity_printers_without_colors} шт\n' \
               f'Сканер с bluetooth: {cls.quantity_scanners_with_bluetooth} шт\n' \
               f'Сканер без bluetooth: {cls.quantity_scanners_without_bluetooth} шт\n' \
               f'Факс с таймером: {cls.quantity_faxes_with_timer} шт\n' \
               f'Факс без таймера: {cls.quantity_faxes_without_timer} шт\n'


class OfficeEquipment:
    def __init__(self, name_model, price, quantity):
        self.name_model = name_model
        self.price = price
        self.quantity = quantity


class Printer(OfficeEquipment):
    def __init__(self, name_model, price, quantity, with_colors):
        super().__init__(name_model, price, quantity)
        self.with_color = with_colors
        if self.with_color is True:
            Stock.quantity_printers_with_colors += int(self.quantity)
        else:
            Stock.quantity_printers_without_colors += int(self.quantity)

    def __str__(self):
        return f'{Printer.__name__} - Название модели: {self.name_model}, Цена: {self.price},' \
               f' Кол-во: {self.quantity}, Цветной: {self.with_color}'


class Scanner(OfficeEquipment):
    def __init__(self, name_model, price, quantity, with_bluetooth):
        super().__init__(name_model, price, quantity)
        self.with_bluetooth = with_bluetooth
        if self.with_bluetooth is True:
            Stock.quantity_scanners_with_bluetooth += int(self.quantity)
        else:
            Stock.quantity_scanners_without_bluetooth += int(self.quantity)

    def __str__(self):
        return f'{Scanner.__name__} - Название модели: {self.name_model}, Цена: {self.price},' \
               f' Кол-во: {self.quantity}, Bluetooth: {self.with_bluetooth}'


class Fax(OfficeEquipment):
    def __init__(self, name_model, price, quantity, with_timer):
        super().__init__(name_model, price, quantity)
        self.with_timer = with_timer
        if self.with_timer is True:
            Stock.quantity_faxes_with_timer += int(self.quantity)
        else:
            Stock.quantity_faxes_without_timer += int(self.quantity)

    def __str__(self):
        return f'{Fax.__name__} - Название модели: {self.name_model}, Цена: {self.price},' \
               f' Кол-во: {self.quantity}, Таймер: {self.with_timer}'


stock_1 = Stock('Склад оргтехники', 'ул.Гагарина, д.10', 'stock@mgail.moc')

printer_1 = Printer('xerox', 15000, 6, True)
scanner_1 = Scanner('canon', 90000, 5, False)
fax_1 = Fax('samsung', 200000, 3, True)
printer_2 = Printer('xerox', 12000, 3, True)
fax_2 = Fax('samsung', 15000, 1, False)

print(stock_1)
print(printer_1)
print(scanner_1)
print(fax_1)
print(Stock.info(stock_1))

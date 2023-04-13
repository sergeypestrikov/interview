# Проверить на практике возможности полиморфизма.
# Необходимо разделить дочерний класс ItemDiscountReport на два класса.
# Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
# которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
# Далее реализовать выполнение каждой из функции тремя способами.


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, val):
        self.__name = val

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def get_price(self, val):
        self.__price = val


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        discount = self.get_price - self.get_price * (self.discount / 100)
        return f'Цена со скидкой: {discount}'

    def set_price(self, price):
        self.__price = price

    def get_parent_data(self):
        print(f'Товар: {self.get_name} цена: {self.get_price}')


class IDRName(ItemDiscount):

    def get_info(self):
        return self.get_name


class IDRPrice(ItemDiscount):

    def get_info(self):
        return self.get_price


if __name__ == '__main__':
    IDRN = IDRName('Тапки', 5)
    IDRP = IDRPrice('Топсайдеры', 30)


    def get_information_1(obj):
        obj.get_info()


    def get_information_2(*args):
        for arg in args:
            arg.get_info()


    get_information_1(IDRN)
    get_information_1(IDRP)

    get_information_2(IDRN, IDRP)

    for obj in (IDRN, IDRP):
        obj.get_info()



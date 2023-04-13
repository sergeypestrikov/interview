# Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента
# в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса
# (метод init, в который должна передаваться переменная — скидка), и перегрузку
# метода str дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат
# — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и
# родительский классы (вторая и третья строка после объявления дочернего класса).


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


ID = ItemDiscount('Ботинки', 25)
ID.get_name, ID.get_price = 'Кроссы', 15
IDR = ItemDiscountReport(ID.get_name, ID.get_price, 30)
IDR.get_parent_data()
print(str(IDR))
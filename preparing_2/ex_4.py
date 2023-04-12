# Реализовать возможность переустановки значения цены товара.
# Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего
# (функция, отвечающая за отображение информации о товаре в одной строке).


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

    def set_price(self, price):
        self.__price = price

    def get_parent_data(self):
        print(f'Товар: {self.get_name} цена: {self.get_price}')


ID = ItemDiscount('Ботинки', 25)
ID.get_name, ID.get_price = 'Кроссы', 13
IDR = ItemDiscountReport(ID.get_name, ID.get_price)
IDR.get_parent_data()
# Усовершенствовать родительский класс таким образом, чтобы получить доступ
# к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'Товар: {self.get_name()} цена: {self.get_price()}')


d = ItemDiscountReport('Ботинки', 25)
d.get_parent_data()
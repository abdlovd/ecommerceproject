from src.task import Category, Product


class CategoryIteration:
    """ Новый вспомогательный класс, с помощью которого можно перебирать
    товары одной категории, например в цикле for. Для этого новый класс
    должен принимать на вход объект класса категории и производить итерацию
    по товарам, которые хранятся в данной категории. То есть метод выполнения
    следующего шага итерации должен возвращать очередной товар категории."""
    def __init__(self, category_object):
        self.object = category_object
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.object.products):
            counting = self.object.products[self.index]
            self.index += 1
            return counting
        else:
            raise StopIteration

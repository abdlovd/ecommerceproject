from src.task import Category, Product


class CategoryIteration:
    def __init__(self, category_object):
        self.category_object = category_object
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category_object.products):
            counting = self.category_object.products[self.index]
            self.index += 1
            return counting
        else:
            raise StopIteration

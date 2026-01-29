from src.task import Category, Product


class CategoryIteration:
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

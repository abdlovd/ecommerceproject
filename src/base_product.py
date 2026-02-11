from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Создайте базовый абстрактный класс с именем BaseProduct,
    который станет родительским для класса продуктов."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

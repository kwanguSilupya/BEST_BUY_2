from products_module import Product
from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        # Buy 2, get 1 free: for every 2 items, one is at half price
        if quantity >= 2:
            return product.price * (quantity - (quantity // 2)) + (product.price * 0.5 * (quantity // 2))
        return product.price * quantity


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        # Buy 2, get 1 free: buy 2, get 1 free (for every 3 items, pay for 2)
        free_items = quantity // 3
        return product.price * (quantity - free_items)


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percent / 100)
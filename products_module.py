class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None  # Initially no promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self):
        promotion_info = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f"{self.name} - ${self.price} - Quantity: {self.quantity} - {promotion_info}"

    def buy(self, quantity):
        if self.promotion:
            price = self.promotion.apply_promotion(self, quantity)
        else:
            price = self.price * quantity
        return price


class NonStockedProduct(Product):
    """A product that does not have stock, e.g., digital goods."""

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def reduce_quantity(self, quantity):
        """Override to prevent quantity changes."""
        if quantity > 0:
            raise ValueError("Non-stocked products cannot have quantity.")

    def show(self):
        return f"{self.name} - ${self.price:.2f} (Non-Stocked)"


class LimitedProduct(Product):
    """A product that has a maximum purchase limit per order."""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def reduce_quantity(self, quantity):
        """Override to enforce maximum purchase limit."""
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} of {self.name} in one order.")
        super().reduce_quantity(quantity)

    def show(self):
        return f"{self.name} - ${self.price:.2f}, Quantity: {self.quantity} (Max {self.maximum} per order)"
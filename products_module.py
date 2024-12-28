class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity

    def is_active(self):
        return self.quantity > 0

    def reduce_quantity(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")
        self.quantity -= quantity

    def show(self):
        return f"{self.name} - ${self.price:.2f}, Quantity: {self.quantity}"


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
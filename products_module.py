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
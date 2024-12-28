class Product:
    def __init__(self, name, price, quantity=0, maximum=None):
        if not name or name.strip() == "":
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.name = name
        self._price = price
        self.quantity = quantity
        self.maximum = maximum
        self.promotion = None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def set_promotion(self, promotion):
        self.promotion = promotion

    def __str__(self):
        return f"{self.name}, Price: ${self.price} Quantity:{self.quantity}"

    def is_active(self):
        """Assumes the product is active if quantity is greater than 0."""
        return self.quantity > 0

# Other classes like NonStockedProduct and LimitedProduct remain unchanged.


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def is_active(self):
        """
        Non-stocked products are always available.
        """
        return True

    def show(self):
        promo_text = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f"{self.name} - ${self.price:.2f} (Non-Stocked) - {promo_text}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def is_active(self):
        """
        Returns True if the product has stock available.
        """
        return self.quantity > 0

    def show(self):
        promo_text = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f"{self.name} - ${self.price:.2f}, Quantity: {self.quantity} (Max {self.maximum} per order) - {promo_text}"

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of this product per order!")
        return super().buy(quantity)
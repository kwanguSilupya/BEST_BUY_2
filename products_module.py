class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None

    def is_active(self):
        """
        Returns True if the product is available for sale.
        """
        return self.quantity > 0

    def set_promotion(self, promotion):
        self.promotion = promotion

    def show(self):
        promo_text = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f"{self.name} - ${self.price} - Quantity: {self.quantity} - {promo_text}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Insufficient stock!")
        self.quantity -= quantity
        if self.promotion:
            return self.promotion.apply_promotion(self.price, quantity)
        return self.price * quantity


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
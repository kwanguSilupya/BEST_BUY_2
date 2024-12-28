from products import Product

class Store:
    def __init__(self, products):
        self.products = products

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def get_total_quantity(self):
        return sum(product.quantity for product in self.products)

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            product.reduce_quantity(quantity)
            total_price += product.price * quantity
        return total_price
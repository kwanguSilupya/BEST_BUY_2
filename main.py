from products_module import Product, NonStockedProduct, LimitedProduct
from store import Store
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount


class Product:
    def __init__(self, name, price, quantity=0, maximum=None):
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

    def __lt__(self, other):
        """Less than comparison based on price."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __gt__(self, other):
        """Greater than comparison based on price."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

    def __eq__(self, other):
        """Equal comparison based on price."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)  # Non-stocked items have no quantity

    def __str__(self):
        return f"{self.name}, Price: ${self.price} (Non-stocked product)"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity, maximum)
        self.maximum = maximum

    def __str__(self):
        return f"{self.name}, Price: ${self.price} Quantity:{self.quantity} (Max: {self.maximum})"


def display_menu():
    """
    Displays the main menu to the user.
    """
    print("\n===== Store Menu =====")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store: Store):
    """
    Lists all active products in the store.
    """
    products = store.get_all_products()
    if not products:
        print("No products available in the store.")
    else:
        print("\nAvailable Products:")
        for i, item in enumerate(products, 1):  # Changed 'product' to 'item' here to avoid confusion
            print(f"{i}. {item}")  # Calls __str__ method for each product


def show_total_quantity(store: Store):
    """
    Displays the total quantity of all products in the store.
    """
    total_quantity = store.get_total_quantity()
    print(f"\nTotal quantity of all products in the store: {total_quantity}")


def make_order(store: Store):
    """
    Handles the process of making an order.
    """
    try:
        list_products(store)
        products = store.get_all_products()

        if not products:
            print("No products available for ordering.")
            return

        shopping_list = []
        while True:
            try:
                product_index = int(input("\nEnter the product number to order (or 0 to finish): ")) - 1
                if product_index == -1:  # User enters 0 to finish
                    break
                if product_index < 0 or product_index >= len(products):
                    print("Invalid product number. Please try again.")
                    continue

                quantity = int(input(f"Enter quantity for {products[product_index].name}: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0. Please try again.")
                    continue

                shopping_list.append((products[product_index], quantity))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if shopping_list:
            try:
                total_price = store.order(shopping_list)
                print(f"\nOrder placed successfully! Total cost: ${total_price:.2f}")
            except Exception as e:
                print(f"Order could not be completed: {e}")

    except KeyboardInterrupt:
        print("\n\nOrder process interrupted by the user. Returning to the main menu.")


def start(store: Store):
    """
    Starts the user interface for the store.
    """
    try:
        while True:
            display_menu()
            choice = input("\nEnter your choice: ").strip()
            if choice == "1":
                list_products(store)
            elif choice == "2":
                show_total_quantity(store)
            elif choice == "3":
                make_order(store)
            elif choice == "4":
                print("Thank you for using the store. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting... Goodbye!")


class Store:
    def __init__(self, products):
        self.products = products

    def get_all_products(self):
        """Returns all active products"""
        return [product for product in self.products if product.is_active()]

    def get_total_quantity(self):
        """Returns the total quantity of all products in the store"""
        return sum(product.quantity for product in self.products)

    def order(self, shopping_list):
        """Handles an order"""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.price * quantity
        return total_price


if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    # Create a store instance
    best_buy = Store(product_list)

    # Start the interactive menu
    start(best_buy)
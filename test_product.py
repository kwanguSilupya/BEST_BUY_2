from products_module import Product, NonStockedProduct, LimitedProduct
import pytest


def test_create_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_non_stocked_product():
    product = NonStockedProduct("Windows License", price=125)
    assert product.quantity == 0  # Non-stocked products should have 0 quantity


def test_limited_product():
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.maximum == 1  # Should only allow one purchase per order
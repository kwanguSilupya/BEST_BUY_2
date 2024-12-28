import pytest
from products_module import Product  # Adjust import if the file name differs

def test_create_normal_product():
    """Test that creating a normal product works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True

def test_create_product_invalid_details():
    """Test that creating a product with invalid details raises an exception."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price

def test_product_becomes_inactive_at_zero_quantity():
    """Test that a product becomes inactive when quantity reaches zero."""
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.reduce_quantity(1)
    assert product.quantity == 0
    assert product.is_active() is False

def test_product_purchase_modifies_quantity():
    """Test that product purchase modifies the quantity correctly."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    product.reduce_quantity(10)
    assert product.quantity == 90
    assert product.is_active() is True

def test_purchase_more_than_available_quantity():
    """Test that buying a larger quantity than exists raises an exception."""
    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(ValueError):
        product.reduce_quantity(10)  # More than available quantity
import pytest
from entities.product import Product
from entities.product_quantity import ProductQuantity, ProductQuantityException

TESTS_QUANTITY_INVALID = ( 0, -1, -2, -10 ) 
TEST_PRODUCT = Product(
  "MILK 1L",
  5.1, 
  "milk a liter", 
  "path-image"
)

TEST_NEW_PRODUCT = Product(
  "Coca-Cola 2L", 
  7.1, 
  "two liter coke", 
  "new-path-image"
)
  
def test_create_product_quantity():
  TEST_QUANTITY = 3
  product_quantity = ProductQuantity(TEST_PRODUCT, TEST_QUANTITY)

  assert product_quantity.get_quantity() == TEST_QUANTITY
  assert product_quantity.get_product() == TEST_PRODUCT
  assert product_quantity.get_name() == TEST_PRODUCT.get_name()


@pytest.mark.parametrize("quantity_invalid", TESTS_QUANTITY_INVALID)
def test_create_product_quantity_error_quantity_invalid(quantity_invalid):
  with pytest.raises(ProductQuantityException):
    ProductQuantity(TEST_PRODUCT, quantity_invalid)


def test_change_data_of_product_quantity():
  TEST_QUANTITY = 3
  TEST_NEW_QUANTITY = 2
  product_quantity = ProductQuantity(TEST_PRODUCT, TEST_QUANTITY)

  product_quantity.set_quantity(TEST_NEW_QUANTITY)
  product_quantity.set_product(TEST_NEW_PRODUCT)

  assert product_quantity.get_quantity() == TEST_NEW_QUANTITY
  assert product_quantity.get_product() == TEST_NEW_PRODUCT
  assert product_quantity.get_name() == TEST_NEW_PRODUCT.get_name()


@pytest.mark.parametrize("quantity_invalid", TESTS_QUANTITY_INVALID)
def test_change_quantity_in_product_quantity_error_quantity_invalid(quantity_invalid):
  TEST_QUANTITY = 3
  product_quantity = ProductQuantity(TEST_PRODUCT, TEST_QUANTITY)

  with pytest.raises(ProductQuantityException):
    product_quantity.set_quantity(quantity_invalid)
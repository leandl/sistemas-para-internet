import pytest

from entities.product import Product

TEST_PRODUCT = {
  "name": "MILK 1L", 
  "price": 5.1, 
  "description": "milk a liter", 
  "path-image": "path-image"
}

TEST_NEW_PRODUCT = {
  "name": "Coca-Cola 2L", 
  "price": 7.1, 
  "description": "two liter coke", 
  "path-image": "new-path-image"
}

def test_create_product():
  product = Product(
    TEST_PRODUCT["name"],
    TEST_PRODUCT["price"],
    TEST_PRODUCT["description"],
    TEST_PRODUCT["path-image"]
  )

  assert product.get_name() == TEST_PRODUCT["name"]
  assert product.get_price() == TEST_PRODUCT["price"]
  assert product.get_description() == TEST_PRODUCT["description"]
  assert product.get_path_image() == TEST_PRODUCT["path-image"]


def test_change_data_of_product():
  product = Product(
    TEST_PRODUCT["name"],
    TEST_PRODUCT["price"],
    TEST_PRODUCT["description"],
    TEST_PRODUCT["path-image"]
  )

  product.set_name(TEST_NEW_PRODUCT["name"])
  product.set_price(TEST_NEW_PRODUCT["price"])
  product.set_description(TEST_NEW_PRODUCT["description"])
  product.set_path_image(TEST_NEW_PRODUCT["path-image"])

  assert product.get_name() == TEST_NEW_PRODUCT["name"]
  assert product.get_price() == TEST_NEW_PRODUCT["price"]
  assert product.get_description() == TEST_NEW_PRODUCT["description"]
  assert product.get_path_image() == TEST_NEW_PRODUCT["path-image"]

import pytest

from entities.little_car import LittleCar, LittleCarException
from entities.product import Product
from entities.product_quantity import ProductQuantity

TEST_LITTLE_CAR_EMPTY = 0

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

TEST_PRODUCT_QUANTITY = ProductQuantity(TEST_PRODUCT, 2)
TEST_PRODUCT_QUANTITY_NEW_QUANTITY = ProductQuantity(TEST_PRODUCT, 5)
TEST_NEW_PRODUCT_QUANTITY = ProductQuantity(TEST_NEW_PRODUCT, 3)


def test_create_little_car():
  PRODUCTS = [TEST_PRODUCT_QUANTITY, TEST_NEW_PRODUCT_QUANTITY]

  little_car = LittleCar(PRODUCTS)
  little_car_empty = LittleCar()

  assert len(little_car.get_products()) == len(PRODUCTS)
  assert little_car.get_products() == PRODUCTS
  assert len(little_car_empty.get_products()) == TEST_LITTLE_CAR_EMPTY



def test_empty_little_car():
  PRODUCTS = [TEST_PRODUCT_QUANTITY, TEST_NEW_PRODUCT_QUANTITY]
  little_car = LittleCar(PRODUCTS)
  little_car.empty()

  assert len(little_car.get_products()) == TEST_LITTLE_CAR_EMPTY



def test_add_product_in_little_car():
  little_car = LittleCar()

  little_car.add_product(TEST_PRODUCT_QUANTITY)
  products = little_car.get_products()
  first_product = products[0] if len(products) == 1 else None

  assert len(products) == 1
  assert first_product == TEST_PRODUCT_QUANTITY

  little_car.add_product(TEST_NEW_PRODUCT_QUANTITY)
  products = little_car.get_products()
  second_product = products[1] if len(products) == 2 else None

  assert len(products) == 2
  assert second_product == TEST_NEW_PRODUCT_QUANTITY



def test_change_quantity_of_product_in_little_car():
  little_car = LittleCar()

  little_car.add_product(TEST_PRODUCT_QUANTITY)
  little_car.add_product(TEST_PRODUCT_QUANTITY_NEW_QUANTITY)

  products = little_car.get_products()
  first_product = products[0] if len(products) == 1 else None

  assert len(products) == 1
  assert first_product == TEST_PRODUCT_QUANTITY_NEW_QUANTITY


def test_remove_product_in_little_car():
  PRODUCTS = [TEST_PRODUCT_QUANTITY, TEST_NEW_PRODUCT_QUANTITY]
  little_car = LittleCar(PRODUCTS)

  little_car.remove_product(TEST_PRODUCT_QUANTITY)
  products = little_car.get_products()
  assert len(products) == 1

  little_car.remove_product(TEST_NEW_PRODUCT_QUANTITY)
  products = little_car.get_products()
  assert len(products) == TEST_LITTLE_CAR_EMPTY

def test_remove_product_in_little_car_error_produt_not_found():
  little_car = LittleCar([TEST_PRODUCT_QUANTITY])
  little_car_empty = LittleCar()

  with pytest.raises(LittleCarException):
    little_car.remove_product(TEST_NEW_PRODUCT_QUANTITY)

  with pytest.raises(LittleCarException):
    little_car_empty.remove_product(TEST_PRODUCT_QUANTITY)
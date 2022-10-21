import pytest
from typing import List
from datetime import datetime

from entities.address import Address
from entities.client import Client
from entities.little_car import LittleCar
from entities.order import Order, OrderException
from entities.product import Product
from entities.product_quantity import ProductQuantity
from entities.status_order import StatusOrder

DATA_DEFAULT_USER = {
  "name": "user-test", 
  "email": "userteste@test.com", 
  "password": "1234", 
}

def factory_create_client(
	phone: str,
	addresses: List[Address],
	little_car: LittleCar = None
) -> Client :
	return Client(
		DATA_DEFAULT_USER["name"],
		DATA_DEFAULT_USER["email"],
		DATA_DEFAULT_USER["password"],
		phone,
		addresses,
		little_car
	)

TEST_ADDRESS = Address("TEST ADDRESS")
TEST_NEW_ADDRESS = Address("TEST NEW ADDRESS")

TEST_PHONE = "(99) 99999-9999"
TEST_NEW_PHONE = "(99) 99999-9999"

TEST_DATE = datetime.fromisoformat('2022-10-20')
TEST_NEW_DATE = datetime.fromisoformat('2022-10-21')

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

TEST_LITTLE_CAR = LittleCar([TEST_PRODUCT_QUANTITY])

TEST_CLIENT = factory_create_client(TEST_PHONE, [TEST_ADDRESS], TEST_LITTLE_CAR)
TEST_NEW_CLIENT = factory_create_client(TEST_NEW_PHONE, [TEST_NEW_ADDRESS])

def test_create_order():
  order = Order(
    TEST_CLIENT,
    TEST_ADDRESS,
    TEST_LITTLE_CAR.get_products(),
    TEST_DATE
  )

  order_with_status = Order(
    TEST_NEW_CLIENT,
    TEST_NEW_ADDRESS,
    TEST_LITTLE_CAR.get_products(),
    TEST_NEW_DATE,
    StatusOrder.DELIVERED
  )

  assert order.get_client() == TEST_CLIENT
  assert order.get_address() == TEST_ADDRESS
  assert order.get_products() == TEST_LITTLE_CAR.get_products()
  assert order.get_date() == TEST_DATE
  assert order.get_status() == StatusOrder.PENDING

  assert order_with_status.get_client() == TEST_NEW_CLIENT
  assert order_with_status.get_address() == TEST_NEW_ADDRESS
  assert order_with_status.get_products() == TEST_LITTLE_CAR.get_products()
  assert order_with_status.get_date() == TEST_NEW_DATE
  assert order_with_status.get_status() == StatusOrder.DELIVERED



def test_create_order_error_quantity_of_products_invalid():
  with pytest.raises(OrderException):
    Order(
      TEST_CLIENT,
      TEST_ADDRESS,
      [],
      TEST_DATE
    )


def test_change_data_order():
  order = Order(
    TEST_CLIENT,
    TEST_ADDRESS,
    TEST_LITTLE_CAR.get_products(),
    TEST_DATE
  )

  order.set_client(TEST_NEW_CLIENT)
  order.set_address(TEST_NEW_ADDRESS)
  order.set_date(TEST_NEW_DATE)
  order.set_status(StatusOrder.CANCELED)

  assert order.get_client() == TEST_NEW_CLIENT
  assert order.get_address() == TEST_NEW_ADDRESS
  assert order.get_date() == TEST_NEW_DATE
  assert order.get_status() == StatusOrder.CANCELED


def test_add_product_in_order():
  little_car = LittleCar([TEST_PRODUCT_QUANTITY])
  order = Order(
    TEST_CLIENT,
    TEST_ADDRESS,
    little_car.get_products(),
    TEST_DATE
  )

  products = order.get_products()
  first_product = products[0] if len(products) == 1 else None

  assert len(products) == 1
  assert first_product == TEST_PRODUCT_QUANTITY

  order.add_product(TEST_NEW_PRODUCT_QUANTITY)
  products = order.get_products()
  second_product = products[1] if len(products) == 2 else None

  assert len(products) == 2
  assert second_product == TEST_NEW_PRODUCT_QUANTITY



def test_change_quantity_of_product_in_order():
  little_car = LittleCar([TEST_PRODUCT_QUANTITY])
  order = Order(
    TEST_CLIENT,
    TEST_ADDRESS,
    little_car.get_products(),
    TEST_DATE
  )

  order.add_product(TEST_PRODUCT_QUANTITY_NEW_QUANTITY)
  products = order.get_products()
  first_product = products[0] if len(products) == 1 else None

  assert len(products) == 1
  assert first_product == TEST_PRODUCT_QUANTITY_NEW_QUANTITY


def test_remove_product_in_order():
  PRODUCTS = [TEST_PRODUCT_QUANTITY, TEST_NEW_PRODUCT_QUANTITY]
  little_car = LittleCar(PRODUCTS)
  order = Order(
    TEST_CLIENT,
    TEST_ADDRESS,
    little_car.get_products(),
    TEST_DATE
  )

  order.remove_product(TEST_PRODUCT_QUANTITY)
  products = order.get_products()
  assert len(products) == 1


def test_remove_product_in_order_error_produt_not_found():
  little_car = LittleCar([TEST_PRODUCT_QUANTITY])
  order = Order(
    TEST_CLIENT,
    TEST_ADDRESS,
    little_car.get_products(),
    TEST_DATE
  )

  with pytest.raises(OrderException):
    order.remove_product(TEST_NEW_PRODUCT_QUANTITY)


def test_remove_product_in_order_error_quantity_of_products_invalid():
  little_car = LittleCar([TEST_PRODUCT_QUANTITY])
  order = Order(
    TEST_CLIENT,
    TEST_ADDRESS,
    little_car.get_products(),
    TEST_DATE
  )

  with pytest.raises(OrderException):
    order.remove_product(TEST_PRODUCT_QUANTITY)
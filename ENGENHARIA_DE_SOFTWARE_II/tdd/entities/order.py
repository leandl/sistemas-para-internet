from typing import List
from datetime import datetime

from entities.address import Address
from entities.client import Client
from entities.product_quantity import ProductQuantity
from entities.status_order import StatusOrder

class OrderException(Exception):
  pass

class Order:

  def __init__(
    self,
    client: Client,
    address: Address,
    products: List[ProductQuantity],
    date: datetime,
    status: StatusOrder = StatusOrder.PENDING
  ) -> None:
    self.__valid_quantity_of_products(products)

    self.__client = client
    self.__address = address
    self.__products = products
    self.__date = date
    self.__status = status

  def __valid_quantity_of_products(self, products: List[ProductQuantity]) -> None:
    if not len(products) > 0:
      raise OrderException("INVALID QUANTITY OF PRODUCTS: 'list of products' cannot be empty")

  def __valid_product_exists(self, product_quantity: ProductQuantity):
    name_products = [product.get_name() for product in self.__products]

    if not product_quantity.get_name() in name_products:
      raise OrderException("PRODUCT NOT FOUND: 'product' not found exists in little car")


  def get_client(self) -> Client:
    return self.__client

  def set_client(self, client: Client) -> None:
    self.__client = client

  def get_address(self) -> Address:
    return self.__address

  def set_address(self, address: Address) -> None:
    self.__address = address

  def get_date(self) -> datetime:
    return self.__date

  def set_date(self, date: datetime) -> None:
    self.__date = date

  def get_status(self) -> StatusOrder:
    return self.__status

  def set_status(self, status: StatusOrder) -> None:
    self.__status = status

  
  def __get_products_without(self, product_quantity: ProductQuantity) -> List[ProductQuantity]:
    product_name = product_quantity.get_name()

    return [
      current_product_quantity
      for current_product_quantity in self.__products
      if current_product_quantity.get_name() != product_name
    ]

  
  def remove_product(self, product_quantity: ProductQuantity) -> None:
    self.__valid_product_exists(product_quantity)
    new_products = self.__get_products_without(product_quantity)

    self.__valid_quantity_of_products(new_products)
    self.__products = new_products

  def add_product(self, product_quantity: ProductQuantity) -> None:
    new_products = self.__get_products_without(product_quantity)
    new_products.append(product_quantity)

    self.__products = new_products

  def get_products(self) -> List[ProductQuantity]:
    return self.__products

  def get_products(self) -> List[ProductQuantity]:
    return self.__products
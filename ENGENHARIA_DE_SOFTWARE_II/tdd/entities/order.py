from typing import List

from datetime import datetime

from entries.address import Address
from entries.client import Client
from entries.product_quantity import ProductQuantity
from entries.status_order import StatusOrder

class Order:

  def __init__(
    self,
    client: Client,
    address: Address,
    products: List[ProductQuantity],
    date: datetime,
    status: StatusOrder = StatusOrder.PENDING
  ) -> None:
    self.__client = client
    self.__address = address
    self.__products = products
    self.__date = date
    self.__status = status

  def get_client(self) -> Client:
    self.__client

  def set_client(self, client: Client) -> None:
    self.__client = client

  def get_address(self) -> Address:
    self.__address

  def set_address(self, address: Address) -> None:
    self.__address = address

  def get_date(self) -> datetime:
    self.__date

  def set_date(self, date: datetime) -> None:
    self.__date = date

  def get_status(self) -> StatusOrder:
    self.__status

  def set_status(self, status: StatusOrder) -> None:
    self.__status = status

  
  def remove_product(
    self,
    product_quantity: ProductQuantity
  ) -> None:
    product_name = product_quantity.get_name()

    self.__products = [
      current_product_quantity
      for current_product_quantity in self.__products
      if current_product_quantity.get_name() == product_name
    ]

  def add_product(
    self,
    product_quantity: ProductQuantity
  ) -> None:
    self.remove_product(product_quantity)
    self.__products.append(product_quantity)

  def get_products(self) -> List[ProductQuantity]:
    return self.__products
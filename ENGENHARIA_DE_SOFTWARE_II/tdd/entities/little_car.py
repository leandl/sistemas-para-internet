from typing import List

from entries.product_quantity import ProductQuantity

class LittleCar:

  def __init__(
    self,
    products: List[ProductQuantity] = None
  ) -> None:
    self.__products = products if products else []

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

  def empty(self) -> None:
    self.__products = []
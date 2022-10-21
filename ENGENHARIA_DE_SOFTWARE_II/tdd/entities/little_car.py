from typing import List

from entities.product_quantity import ProductQuantity

class LittleCarException(Exception):
  pass

class LittleCar:

  def __init__(self, products: List[ProductQuantity] = None) -> None:
    self.__products = products if products else []

  def __valid_product_exists(self, product_quantity: ProductQuantity):
    name_products = [product.get_name() for product in self.__products]

    if not product_quantity.get_name() in name_products:
      raise LittleCarException("PRODUCT NOT FOUND: 'product' not found exists in little car")



  def __get_products_without(
    self,
    product_quantity: ProductQuantity
  ) -> List[ProductQuantity]:
    product_name = product_quantity.get_name()

    return [
      current_product_quantity
      for current_product_quantity in self.__products
      if current_product_quantity.get_name() != product_name
    ]


  def remove_product(self, product_quantity: ProductQuantity) -> None:
    self.__valid_product_exists(product_quantity)
    self.__products = self.__get_products_without(product_quantity)

  def add_product(self, product_quantity: ProductQuantity) -> None:
    new_products = self.__get_products_without(product_quantity)
    new_products.append(product_quantity)

    print(new_products)
    self.__products = new_products

  def get_products(self) -> List[ProductQuantity]:
    return self.__products

  def empty(self) -> None:
    self.__products = []

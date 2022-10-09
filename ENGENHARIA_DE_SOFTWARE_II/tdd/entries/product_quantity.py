from entries.product import Product

class ProductQauntityException(Exception):
  pass

class ProductQuantity:

  def __init__(
    self,
    product: Product,
    quantity: int
  ) -> None:
    self.__valid_product_quantity(quantity)

    self.__product = product
    self.__quantity = quantity

  def __valid_product_quantity(self, quantity: int) -> None:
    MIN_PRODUCT_QUANTITY = 1

    if quantity < MIN_PRODUCT_QUANTITY:
      raise ProductQauntityException("Quatity invalid!!")

  def get_product(self) -> Product:
    self.__product

  def set_product(self, product: Product) -> None:
    self.__product = product

  def get_quantity(self) -> int:
    self.__quantity

  def set_quantity(self, quantity: int) -> None:
    self.__valid_product_quantity(quantity)

    self.__quantity = quantity
  
  def get_name(self) -> str:
    self.__product.get_name()
from entities.product import Product

class ProductQuantityException(Exception):
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

    if not quantity >= MIN_PRODUCT_QUANTITY:
      raise ProductQuantityException("QUANTITY INVALID: 'quantity' must be greater than zero")

  def get_product(self) -> Product:
    return self.__product

  def set_product(self, product: Product) -> None:
    self.__product = product

  def get_quantity(self) -> int:
    return self.__quantity

  def set_quantity(self, quantity: int) -> None:
    self.__valid_product_quantity(quantity)

    self.__quantity = quantity
  
  def get_name(self) -> str:
    return self.__product.get_name()
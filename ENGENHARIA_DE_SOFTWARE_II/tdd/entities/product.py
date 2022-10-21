class ProductException(Exception):
  pass

class Product:

  def __init__(
    self,
    name: str,
    price: float,
    description: str,
    path_image: str
  ) -> None:
    self.__valid_price(price)

    self.__name = name
    self.__price = price
    self.__description = description
    self.__path_image = path_image

  def __valid_price(self, price: float):
    if not price > 0:
      raise ProductException("INVALID PRICE: 'price' must be greater than zero")

  def get_name(self) -> str:
    return self.__name

  def set_name(self, name: str) -> None:
    self.__name = name

  def get_price(self) -> float:
    return self.__price

  def set_price(self, price: float) -> None:
    self.__valid_price(price)
    self.__price = price

  def get_description(self) -> str:
    return self.__description

  def set_description(self, description: str) -> None:
    self.__description = description

  def get_path_image(self) -> str:
    return self.__path_image

  def set_path_image(self, path_image: str) -> None:
    self.__path_image = path_image

  def __str__(self) -> str:
    return f"Product(name: {self.__name}, price: {self.__price}, description: {self.__description}, path_image: {self.__path_image})"
class Address:

  def __init__(self, address: str) -> None:
    self.__address = address

  def get_address(self) -> str:
    return self.__address

  def set_address(self, address: str) -> None:
    self.__address = address

  def __str__(self) -> str:
    return f"Address({self.__address})"
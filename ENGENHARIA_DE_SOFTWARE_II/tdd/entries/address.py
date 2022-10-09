class Address:

  def __init__(self, address: str) -> None:
    self.__address = address

  def get_address(self) -> str:
    self.__address

  def set_address(self, address: str) -> None:
    self.__address = address
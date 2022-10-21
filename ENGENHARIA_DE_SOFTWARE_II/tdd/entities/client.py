from typing import List

from entities.address import Address
from entities.little_car import LittleCar
from entities.user import User

class ClientException(Exception):
  pass

class Client(User):

  def __init__(
    self,
    name: str,
    email: str,
    password: str,
    phone: str,
    addresses: List[Address],
    little_car: LittleCar = None
  ) -> None:
    self.__valid_quantity_of_addresses(addresses)

    super().__init__(name, email, password)

    self.__phone = phone
    self.__addresses = addresses
    self.__little_car = little_car if little_car else LittleCar()

  def __valid_quantity_of_addresses(self, addresses: List[Address]) -> None:
    if not len(addresses) > 0:
      raise ClientException("INVALID QUANTITY OF ADDRESSES: 'list of addresses' cannot be empty")

  def get_phone(self) -> str:
    return self.__phone

  def set_phone(self, phone: str) -> None:
    self.__phone = phone

  def remove_address(self, address: Address) -> None:
    new_addresses: List[Address] = [
      current_address
      for current_address in self.__addresses
      if current_address.get_address() != address.get_address()
    ]

    self.__valid_quantity_of_addresses(new_addresses)
    self.__addresses = new_addresses 

  def add_address(self, address: Address) -> None:
    self.remove_address(address)
    self.__addresses.append(address)

  def get_addresses(self) -> List[Address]:
    return self.__addresses

  def get_little_car(self) -> LittleCar:
    return self.__little_car

  
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
    if len(addresses) == 0:
      raise ClientException("")

    super().__init__(name, email, password)

    self.__phone = phone
    self.__addresses = addresses
    self.__little_car = little_car if little_car else LittleCar()

  def get_phone(self) -> str:
    self.__phone

  def set_phone(self, phone: str) -> None:
    self.__phone = phone

  def remove_address(self, address: Address) -> None:
    self.__addresses: List[Address] = [
      current_address
      for current_address in self.__addresses
      if current_address.get_address() == address.get_address()
    ]

  def add_address(self, address: Address) -> None:
    self.remove_address(address)
    self.__addresses.append(address)

  def get_addresses(self) -> List[Address]:
    return self.__addresses

  def get_little_car(self) -> LittleCar:
    self.__little_car

  
import re

class UserException(Exception):
  pass

class User:

  def __init__(
    self,
    name: str,
    email: str,
    password: str
  ) -> None:
    self.__valid_email(email)

    self.__name = name
    self.__email = email
    self.__password = password

  def __valid_email(self, email: str):
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex_email, email):
      raise UserException("INVALID E-MAIL: invalid e-mail syntax")


  def get_name(self) -> str:
    return self.__name

  def set_name(self, name: str) -> None:
    self.__name = name

  def get_email(self) -> str:
    return self.__email

  def set_email(self, email: str) -> None:
    self.__valid_email(email)
    self.__email = email

  def get_password(self) -> str:
    return self.__password

  def set_password(self, password: str) -> None:
    self.__password = password

  def __str__(self) -> str:
    return f"User(name: {self.__name}, email: {self.__email}, password: {self.__password})"
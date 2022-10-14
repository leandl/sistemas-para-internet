
class User:

  def __init__(
    self,
    name: str,
    email: str,
    password: str
  ) -> None:
    self.__name = name
    self.__email = email
    self.__password = password

  def get_name(self) -> str:
    return self.__name

  def set_name(self, name: str) -> None:
    self.__name = name

  def get_email(self) -> str:
    return self.__email

  def set_email(self, email: str) -> None:
    self.__email = email

  def get_password(self) -> str:
    return self.__password

  def set_password(self, password: str) -> None:
    self.__password = password
import pytest
from entities.user import User

TEST_USER = {
  "name": "user-test", 
  "email": "userteste@test.com", 
  "password": "1234", 
}

TEST_NEW_USER = {
  "name": "new-user-test", 
  "email": "newuserteste@test.com", 
  "password": "3215", 
}

def test_create_user():
  product = User(
    TEST_USER["name"],
    TEST_USER["email"],
    TEST_USER["password"],
  )

  assert product.get_name() == TEST_USER["name"]
  assert product.get_email() == TEST_USER["email"]
  assert product.get_password() == TEST_USER["password"]


def test_change_data_of_user():
  product = User(
    TEST_USER["name"],
    TEST_USER["email"],
    TEST_USER["password"],
  )

  product.set_name(TEST_NEW_USER["name"])
  product.set_email(TEST_NEW_USER["email"])
  product.set_password(TEST_NEW_USER["password"])

  assert product.get_name() == TEST_NEW_USER["name"]
  assert product.get_email() == TEST_NEW_USER["email"]
  assert product.get_password() == TEST_NEW_USER["password"]
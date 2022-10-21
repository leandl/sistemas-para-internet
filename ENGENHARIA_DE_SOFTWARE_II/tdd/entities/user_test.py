import pytest
from entities.user import User, UserException

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

TEST_EMAILS_INVALID = (
  "email",
  "tony.example.com",
  "tony@stark@example.net",
  "tony@.example.co.uk",
  "@."
)

def test_create_user():
  product = User(
    TEST_USER["name"],
    TEST_USER["email"],
    TEST_USER["password"],
  )

  assert product.get_name() == TEST_USER["name"]
  assert product.get_email() == TEST_USER["email"]
  assert product.get_password() == TEST_USER["password"]



@pytest.mark.parametrize("email_invalid", TEST_EMAILS_INVALID)
def test_create_user_error_email_invalid(email_invalid):
  with pytest.raises(UserException):
    User(
      TEST_USER["name"],
      email_invalid,
      TEST_USER["password"],
    )



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



@pytest.mark.parametrize("email_invalid", TEST_EMAILS_INVALID)
def test_change_data_of_user_error_email_invalid(email_invalid):
  product = User(
    TEST_USER["name"],
    TEST_USER["email"],
    TEST_USER["password"],
  )
  with pytest.raises(UserException):
    product.set_email(email_invalid)
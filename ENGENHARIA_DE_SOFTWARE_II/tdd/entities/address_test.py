import pytest
from entities.address import Address


def test_create_address():
  TEST_ADDRESS = "TEST ADDRESS"

  address = Address(TEST_ADDRESS)
  assert address.get_address() == TEST_ADDRESS
  
def test_create_address():
  TEST_ADDRESS = "TEST ADDRESS"
  TEST_NEW_ADDRESS = "TEST NEW ADDRESS"

  address = Address(TEST_ADDRESS)
  address.set_address(TEST_NEW_ADDRESS)
  assert address.get_address() == TEST_NEW_ADDRESS
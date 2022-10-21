import pytest
from typing import List

from entities.address import Address
from entities.client import Client, ClientException
from entities.little_car import LittleCar

DATA_DEFAULT_USER = {
  "name": "user-test", 
  "email": "userteste@test.com", 
  "password": "1234", 
}

def factory_create_client(
	phone: str,
	addresses: List[Address],
	little_car: LittleCar = None
) -> Client :
	return Client(
		DATA_DEFAULT_USER["name"],
		DATA_DEFAULT_USER["email"],
		DATA_DEFAULT_USER["password"],
		phone,
		addresses,
		little_car
	) 

TEST_ADDRESS_1 = Address("TEST ADDRESS 1")
TEST_ADDRESS_2 = Address("TEST ADDRESS 2")

TEST_PHONE = "(99) 99999-9999"
TEST_NEW_PHONE = "(99) 99999-9999"

TEST_LITTLE_CAR = LittleCar()

def test_create_client():
	TEST_ONE_ADDRESS = 1
	TEST_LITTLE_CAR_EMPTY = 0

	client_with_little_car = factory_create_client(TEST_PHONE, [TEST_ADDRESS_1], TEST_LITTLE_CAR)
	client_without_little_car = factory_create_client(TEST_PHONE, [TEST_ADDRESS_2])
	
	assert client_with_little_car.get_phone() == TEST_PHONE
	assert client_without_little_car.get_phone() == TEST_PHONE

	addresses_client_with_little_car = client_with_little_car.get_addresses()
	addresses_client_without_little_car = client_without_little_car.get_addresses()

	assert len(addresses_client_with_little_car) == TEST_ONE_ADDRESS
	assert len(addresses_client_without_little_car) == TEST_ONE_ADDRESS

	first_address_client_with_little_car = addresses_client_with_little_car[0] if len(addresses_client_with_little_car) else None
	first_address_client_without_little_car = addresses_client_without_little_car[0] if len(addresses_client_with_little_car) else None

	assert first_address_client_with_little_car == TEST_ADDRESS_1
	assert first_address_client_without_little_car == TEST_ADDRESS_2

	little_car_client_with_little_car = client_with_little_car.get_little_car()
	little_car_client_without_little_car = client_without_little_car.get_little_car()

	assert len(little_car_client_with_little_car.get_products()) == TEST_LITTLE_CAR_EMPTY
	assert len(little_car_client_without_little_car.get_products()) == TEST_LITTLE_CAR_EMPTY

def test_create_client_error_quantity_of_addresses_invalid():
	with pytest.raises(ClientException):
		factory_create_client(TEST_PHONE, [])

def test_change_data_client():
	client = factory_create_client(TEST_PHONE, [TEST_ADDRESS_1])

	client.set_phone(TEST_NEW_PHONE)
	client.add_address(TEST_ADDRESS_2)

	assert client.get_phone() == TEST_NEW_PHONE

	addresses_client = client.get_addresses()
	first_address = addresses_client[0] if len(addresses_client) == 2 else None
	second_address = addresses_client[1] if len(addresses_client) == 2 else None

	assert first_address == TEST_ADDRESS_1
	assert second_address == TEST_ADDRESS_2

	client.remove_address(TEST_ADDRESS_1)

	addresses_client = client.get_addresses()
	first_address = addresses_client[0] if len(addresses_client) == 1 else None
	
	assert first_address ==  TEST_ADDRESS_2

	
def test_change_data_client_error_quantity_of_addresses_invalid():
	client = factory_create_client(TEST_PHONE, [TEST_ADDRESS_1])
	with pytest.raises(ClientException):
		client.remove_address(TEST_ADDRESS_1)
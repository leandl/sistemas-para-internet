from entities.little_car import LittleCar
from entities.product import Product
from entities.product_quantity import ProductQuantity


if __name__ == "__main__":
  print("Running system")

  product = Product("arroz", 1.2, "description", "path_image")
  myLittleCar = LittleCar()

  LittleCar.add_product(ProductQuantity(product, 2))
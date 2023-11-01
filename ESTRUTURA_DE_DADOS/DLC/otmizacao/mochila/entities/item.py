class Item:
    def __init__(self, name: str, volume: float, price: float) -> None:
        self.__name = name
        self.__volume = volume
        self.__price = price

    def get_name(self) -> str:
        return self.__name
    
    def get_volume(self) -> float:
        return self.__volume
    

    def get_price(self) -> float:
        return self.__price
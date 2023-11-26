import random
from typing import List, Tuple

from .item import Item
from config import Config
from crossovers import crossover_chromossomes

random_zero_or_one = lambda _x: random.choice([0, 1])
random_min_to_max = lambda min, max: random.randrange(min, max)

class Individual:

    def __init__(
        self,
        items: List["Item"],
        volume_limit: int,
        generation: int = 0,
        chromossomes: List[int] = None
    ) -> None:
        self.__items = items
        self.__generation = generation
        self.__volume_limit = volume_limit

        self.__chromossomes = chromossomes if chromossomes is not None else[random_zero_or_one(i) for i in self.__items]
        
        volume, price = self.__generate_data_individual(self.__items, self.__chromossomes)
        self.__price = price
        self.__volume = volume
        self.__score = self.__generate_score(volume_limit, price, volume)    

        
    def __generate_data_individual(self, items: List["Item"], chromossomes: List[int]) -> Tuple[float, float]:
        volume = 0
        price = 0

        for index, item in enumerate(items):
            if chromossomes[index] == 1:
                volume += item.get_volume()
                price += item.get_price()

        return volume, price
        

    
    def __generate_score(self, volume_limit: int, price: float, volume: float):
        if volume > volume_limit:
            return 1.0
        
        return price
    
    def get_chromossomes(self) -> List[int]:
        return self.__chromossomes
    
    def get_score(self) -> float:
        return self.__score
    
    def get_price(self) -> float:
        return self.__price
        
    def get_volume(self) -> float:
        return self.__volume
    
    def crossover(self, other_individual: "Individual") -> Tuple["Individual", "Individual"]:
        current_chromossomes = self.__chromossomes
        other_chromossomes = other_individual.get_chromossomes()

        generate_crossover = crossover_chromossomes[Config.TYPE_CROSSOVER]
        chromossomes_f1, chromossomes_f2 = generate_crossover(current_chromossomes, other_chromossomes)

        return (
            Individual(
                self.__items,
                self.__volume_limit,
                self.__generation + 1,
                self.__mutation(chromossomes_f1)
            ),
            Individual(
                self.__items,
                self.__volume_limit,
                self.__generation + 1,
                self.__mutation(chromossomes_f2)
            )
        )
    
    def __mutation(self, chromossomes: List[int]) -> List[int]:

        
        for index, d in enumerate(chromossomes):
            if Config.MUTATION_RATE < random_min_to_max(1, 1000):
                continue
            
            chromossomes[index] = 1 if d == 0 else 0
                
        return chromossomes

        

    def __str__(self) -> str:
        return self.__chromossomes.__str__()
    

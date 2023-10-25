import random


random_zero_or_one = lambda _x: random.choice([0, 1])

class Individual:

    def __init__(self, items, volume_limit, generation = 0) -> None:
        self.items = items
        self.generation = generation
        self.volume_limit = volume_limit

        self.__generate_chromossomes()
        self.__generate_data_individual()
        self.__generate_score()    
    


    def __generate_chromossomes(self):
        self.chromossomes = [random_zero_or_one(i) for i in self.items]

         
    def __generate_data_individual(self, items, chromossomes):
        self.volume = 0
        self.price = 0

        for index, item in enumerate(items):
            if chromossomes[index] == 1:
                self.volume += item.get_volume()
                self.price += item.get_price()
    
    def __generate_score(self):
        self.score = 0
        if self.volume > self.volume_limit:
            self.score = 0
            return
        
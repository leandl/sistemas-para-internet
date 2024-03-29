import random
import math
from typing import List

from utls import compare_item, revert_compare
from config import Config

from entities.individual import Individual
from entities.ordered_vertor import OrderedVector

class GeneticAlgorithm:

    @staticmethod
    def execute(items, amount_individual, n_generation) -> List["Individual"]:
    
        best_individuals = []

        population = OrderedVector(amount_individual, revert_compare(compare_item))

        for _ in range(amount_individual):
            population.insert(Individual(items, Config.BAG_VOLUME_LIMIT))

        
        for _ in range(n_generation):
            best_individuals.append(population.get(0))
            new_population = OrderedVector(amount_individual, revert_compare(compare_item))
            score = GeneticAlgorithm.__score_population(population)

            population_random = GeneticAlgorithm.__get_individuals_random(population, score)

            for index in range(amount_individual // 2):
                last_index = index + 1
                individual1 = population_random[index]
                individual2 = population_random[last_index]

                f1, f2 = individual1.crossover(individual2)

                new_population.insert(f1)
                new_population.insert(f2)

            population = new_population
        
        best_individuals.append(population.get(0))
        return best_individuals
    
    @staticmethod
    def __score_population(population: "OrderedVector") -> float:
        return sum([ i.get_score() for i in population ])
    

    @staticmethod
    def __get_individual_random(population: "OrderedVector", score_population: float):
        n = random.randrange(math.floor(score_population))
        sun = 0
        
        for index in range(len(population)):
            i = population.get(index)

            sun += i.get_score()
            if sun >= n:
                return i
        
        return population.get(0)
    
    @staticmethod
    def __get_individuals_random(population: "OrderedVector", score_population: float):
        return [ 
            GeneticAlgorithm.__get_individual_random(
                population,
                score_population
            ) for _ in range(len(population))
        ]
        

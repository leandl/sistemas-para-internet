from items import items
from utls import compare_item, revert_compare

from entities.individual import Individual
from entities.ordered_vertor import OrderedVector

BAG_VOLUME = 10

class GeneticAlgorithm:

    @staticmethod
    def execute(amount_individual, n_generation):
        m = amount_individual // 2
        orderedVector = OrderedVector(amount_individual * n_generation, revert_compare(compare_item))
        for _ in range(amount_individual):
            orderedVector.insert(Individual(items, BAG_VOLUME))

        
        for _ in range(n_generation):
            
            for index in range(m // 2):
                last_index = m - index
                individual1 = orderedVector.get(index)
                individual2 = orderedVector.get(last_index)

                f1, f2 = individual1.crossover(individual2)

                orderedVector.insert(f1)
                orderedVector.insert(f2)
            
            
        


        return orderedVector.get(0)
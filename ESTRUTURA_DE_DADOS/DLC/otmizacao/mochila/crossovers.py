from typing import List, Tuple
import random

random_min_to_max = lambda min, max: random.randrange(min, max)

def crossover_random(chromossomes1: List[int], chromossomes2: List[int]) -> Tuple[List[int], List[int]]: 
    index_crossover = random_min_to_max(0, len(chromossomes1))

    chromossomes_f1 = chromossomes1[:index_crossover] + chromossomes2[index_crossover:]
    chromossomes_f2 = chromossomes2[:index_crossover] + chromossomes1[index_crossover:]

    return chromossomes_f1, chromossomes_f2



def crossover_center(chromossomes1: List[int], chromossomes2: List[int]) -> Tuple[List[int], List[int]]: 
    index_crossover = round(len(chromossomes1) / 2)

    chromossomes_f1 = chromossomes1[:index_crossover] + chromossomes2[index_crossover:]
    chromossomes_f2 = chromossomes2[:index_crossover] + chromossomes1[index_crossover:]

    return chromossomes_f1, chromossomes_f2



def crossover_two_pivots(chromossomes1: List[int], chromossomes2: List[int]) -> Tuple[List[int], List[int]]: 
    index_center = round(len(chromossomes1) / 2)
    half_center = round(index_center/ 2)

    index_crossover_1 = index_center - half_center
    index_crossover_2 = index_center + half_center

    chromossomes_f1 = chromossomes1[:index_crossover_1] + chromossomes2[index_crossover_1:index_crossover_2] + chromossomes1[index_crossover_2:] 
    chromossomes_f2 = chromossomes2[:index_crossover_1] + chromossomes1[index_crossover_1:index_crossover_2] + chromossomes2[index_crossover_2:]

    return chromossomes_f1, chromossomes_f2



crossover_chromossomes = {
    "random": crossover_random,
    "center": crossover_center,
    "two-pivots": crossover_two_pivots
}

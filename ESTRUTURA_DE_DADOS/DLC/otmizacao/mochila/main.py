import matplotlib.pyplot as plt
from genetic_algorithm import GeneticAlgorithm
from config import Config


def run(ax):
    best_individuals = GeneticAlgorithm.execute(
    Config.NUMBER_OF_INDIVIDUAL_BY_POPULATION,
    Config.NUMBER_OF_GENERATIONS
    )

    ax.plot(
        [ generation for generation in range(len(best_individuals)) ],
        [ individual.get_price() for individual in best_individuals ],
    )
  

INDEX_NUMBER_OF_GENERATIONS = 0
INDEX_NUMBER_OF_INDIVIDUAL_BY_POPULATION = 1
INDEX_MUTATION_RATE = 2
data_testes = [
    [10, 50, 100, 150],
    [10, 30, 50, 100],
    [1, 2, 3, 5, 10]
]


for MUTATION_RATE in data_testes[INDEX_MUTATION_RATE]:
    fig, axes = plt.subplots(4, 4, figsize=(10, 5))
    fig.suptitle(f"Taxa de Mutação: {MUTATION_RATE}")
    for row, NUMBER_OF_GENERATIONS in enumerate(data_testes[INDEX_NUMBER_OF_GENERATIONS]):
        for col, NUMBER_OF_INDIVIDUAL_BY_POPULATION  in enumerate(data_testes[INDEX_NUMBER_OF_INDIVIDUAL_BY_POPULATION]):
            Config.NUMBER_OF_GENERATIONS = NUMBER_OF_GENERATIONS
            Config.NUMBER_OF_INDIVIDUAL_BY_POPULATION = NUMBER_OF_INDIVIDUAL_BY_POPULATION
            Config.MUTATION_RATE = MUTATION_RATE
            run(axes[row][col])


plt.show()

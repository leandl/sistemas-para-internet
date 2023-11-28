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
  

# INDEX_NUMBER_OF_GENERATIONS = 0
# INDEX_NUMBER_OF_INDIVIDUAL_BY_POPULATION = 1
# INDEX_MUTATION_RATE = 2
# data_testes = [
#     [10, 50, 100, 150],
#     [10, 30, 50, 100],
#     [1, 2, 3, 5, 10]
# ]


# for MUTATION_RATE in data_testes[INDEX_MUTATION_RATE]:
#     fig, axes = plt.subplots(4, 4, figsize=(10, 5))
#     fig.suptitle(f"Taxa de Mutação: {MUTATION_RATE}")
#     for row, NUMBER_OF_GENERATIONS in enumerate(data_testes[INDEX_NUMBER_OF_GENERATIONS]):
#         for col, NUMBER_OF_INDIVIDUAL_BY_POPULATION  in enumerate(data_testes[INDEX_NUMBER_OF_INDIVIDUAL_BY_POPULATION]):
#             Config.NUMBER_OF_GENERATIONS = NUMBER_OF_GENERATIONS
#             Config.NUMBER_OF_INDIVIDUAL_BY_POPULATION = NUMBER_OF_INDIVIDUAL_BY_POPULATION
#             Config.MUTATION_RATE = MUTATION_RATE
#             run(axes[row][col])





# tests_mutation = [1, 5, 10, 20, 50, 100] # escala 1/1000
# fig, axes = plt.subplots(1, 6, figsize=(10, 5))
# for index, MUTATION_RATE in enumerate(tests_mutation):
#     fig.suptitle(f"Testes de Mutação")
#     Config.MUTATION_RATE = MUTATION_RATE

#     percentage = (MUTATION_RATE / 10) 

#     axes[index].set_title(f"Taxa de mutação: {percentage}")
#     axes[index].set_xlabel('Gerações')
#     axes[index].set_ylabel('Preço')
#     run(axes[index])


# tests_number_of_generations = [5, 10, 20, 50, 100, 200] 
# fig, axes = plt.subplots(1, 6, figsize=(10, 5))
# for index, NUMBER_OF_GENERATIONS in enumerate(tests_number_of_generations):
#     fig.suptitle(f"Testes de Número de Gerações")
#     Config.NUMBER_OF_GENERATIONS = NUMBER_OF_GENERATIONS


#     axes[index].set_title(f"Número de Gerações: {NUMBER_OF_GENERATIONS}")
#     axes[index].set_xlabel('Gerações')
#     axes[index].set_ylabel('Preço')
#     run(axes[index])


# tests_number_of_individual_by_population = [5, 10, 20, 50, 100, 200] 
# fig, axes = plt.subplots(1, 6, figsize=(10, 5))
# for index, NUMBER_OF_INDIVIDUAL_BY_POPULATION  in enumerate(tests_number_of_individual_by_population):
#     fig.suptitle(f"Testes de Número de individual de População")
#     Config.NUMBER_OF_INDIVIDUAL_BY_POPULATION  = NUMBER_OF_INDIVIDUAL_BY_POPULATION 


#     axes[index].set_title(f"Número de individual\n por População: {NUMBER_OF_INDIVIDUAL_BY_POPULATION }")
#     axes[index].set_xlabel('Gerações')
#     axes[index].set_ylabel('Preço')
#     run(axes[index])


tests_type_crossover = ["two-pivots", "random", "center"] 
fig, axes = plt.subplots(1, 3, figsize=(10, 5))
for index, TYPE_CROSSOVER  in enumerate(tests_type_crossover):
    fig.suptitle(f"Testes de Tipo de Cruzamento")
    Config.TYPE_CROSSOVER  = TYPE_CROSSOVER 


    axes[index].set_title(f"Tipo de Cruzamento: {TYPE_CROSSOVER }")
    axes[index].set_xlabel('Gerações')
    axes[index].set_ylabel('Preço')
    run(axes[index])


plt.show()
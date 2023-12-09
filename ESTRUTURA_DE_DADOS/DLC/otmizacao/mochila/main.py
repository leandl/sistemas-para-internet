import matplotlib.pyplot as plt
from genetic_algorithm import GeneticAlgorithm
from config import Config
from items import items_5, items_10, items_default, items_all


def run(ax, items):
    best_individuals = GeneticAlgorithm.execute(
        items,
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
# fig.suptitle(f"Testes de Mutação")
# for index, MUTATION_RATE in enumerate(tests_mutation):
#     Config.MUTATION_RATE = MUTATION_RATE

#     percentage = (MUTATION_RATE / 10) 

#     axes[index].set_title(f"Taxa de mutação: {percentage}")
#     axes[index].set_xlabel('Gerações')
#     axes[index].set_ylabel('Preço')
#     run(axes[index], items_default)


# tests_number_of_generations = [5, 10, 20, 50, 100, 200] 
# fig, axes = plt.subplots(1, 6, figsize=(10, 5))
# fig.suptitle(f"Testes de Número de Gerações")
# for index, NUMBER_OF_GENERATIONS in enumerate(tests_number_of_generations):
#     Config.NUMBER_OF_GENERATIONS = NUMBER_OF_GENERATIONS


#     axes[index].set_title(f"Número de Gerações: {NUMBER_OF_GENERATIONS}")
#     axes[index].set_xlabel('Gerações')
#     axes[index].set_ylabel('Preço')
#     run(axes[index], items_default)


# tests_number_of_individual_by_population = [5, 10, 20, 50, 100, 200] 
# fig, axes = plt.subplots(1, 6, figsize=(10, 5))
# fig.suptitle(f"Testes de Número de individual de População")
# for index, NUMBER_OF_INDIVIDUAL_BY_POPULATION  in enumerate(tests_number_of_individual_by_population):
#     Config.NUMBER_OF_INDIVIDUAL_BY_POPULATION  = NUMBER_OF_INDIVIDUAL_BY_POPULATION 


#     axes[index].set_title(f"Número de individual\n por População: {NUMBER_OF_INDIVIDUAL_BY_POPULATION}")
#     axes[index].set_xlabel('Gerações')
#     axes[index].set_ylabel('Preço')
#     run(axes[index], items_default)


# tests_type_crossover = ["two-pivots", "random", "center"] 
# fig, axes = plt.subplots(1, 3, figsize=(10, 5))
# fig.suptitle(f"Testes de Tipo de Cruzamento")
# for index, TYPE_CROSSOVER  in enumerate(tests_type_crossover):
#     Config.TYPE_CROSSOVER  = TYPE_CROSSOVER 


#     axes[index].set_title(f"Tipo de Cruzamento: {TYPE_CROSSOVER}")
#     axes[index].set_xlabel('Gerações')
#     axes[index].set_ylabel('Preço')
#     run(axes[index], items_default)


# tests_items = [items_5, items_10, items_default, items_all] 
# fig, axes = plt.subplots(1, 4, figsize=(10, 5))
# fig.suptitle(f"Testes com Números de Produtos")
# for index, items  in enumerate(tests_items):
#     count_items = len(items)

#     axes[index].set_title(f"Números de Produtos: {count_items}")
#     axes[index].set_xlabel('Gerações')
#     axes[index].set_ylabel('Preço')
#     run(axes[index], items)

run(plt, items_default)
plt.show()

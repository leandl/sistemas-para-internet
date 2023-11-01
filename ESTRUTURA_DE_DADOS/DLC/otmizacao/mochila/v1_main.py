import itertools
import timeit 

products = [
    ("Arroz", 1.11, 4.75),
    ("Feijao", 1.25, 8.00),
    ("Farinha de trigo", 1.67, 5.50),
    ("Acucar", 1.25, 3.50),
    ("Sal", 0.46, 1.50),
    ("Oleo de cozinha", 0.9, 4.50),
    ("Cafe", 1.39, 16.00),
    ("Leite", 1.00, 3.75),
    ("Manteiga", 0.54, 11.50),
    ("Pao", 1.75, 10.00),
    ("Massas", 1.33, 7.50),
    ("Enlatados", 0.33, 6.00),
    ("Sabao", 0.22, 3.00),
    ("Papel higienico", 3.24, 4.50),
    ("Sorvete", 1.00, 23.00),
    ("Creme de Leite", 0.50, 4.50),
]


NAME = 0
VOLUME = 1
PRICE = 2

start = timeit.default_timer()

def generate_data(combination = []):
    volume = 0
    price = 0
    for p in combination:
        volume += p[VOLUME]
        price += p[PRICE]


    return {
        "volume": volume,
        "price": price,
        "combination": combination
    }


ALL_COMBINATIONS = []
total = 0
for i in range(0, len(products)):
    all_combinations = []
    for combination in itertools.combinations(products, i):
        all_combinations.append(
            generate_data(combination)
        )

    ALL_COMBINATIONS.append(all_combinations)
    total += len(all_combinations)

current = ALL_COMBINATIONS[0][0]
for combinations in ALL_COMBINATIONS:
    for combination in combinations:
        if combination.get("volume", 11) <= 10 and current.get("price") < combination.get("price"):
            current = combination


print(total)
print(current)
print(timeit.default_timer() - start)
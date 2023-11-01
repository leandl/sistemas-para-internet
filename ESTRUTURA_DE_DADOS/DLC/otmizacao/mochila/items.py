from entities.item import Item

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

items = [ Item(*p) for p in products ]

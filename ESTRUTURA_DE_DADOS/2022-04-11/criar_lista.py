import timeit

def criar_lista(n):
    return list(range(0, n+1))

tempo_inicial = timeit.default_timer()
lista = criar_lista(999)
tempo_final = timeit.default_timer()

print(tempo_final - tempo_inicial)
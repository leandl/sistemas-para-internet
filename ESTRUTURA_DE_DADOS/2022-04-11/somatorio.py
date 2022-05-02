import timeit

def somatorio(n): 
    if n == 1:
        return 1

    return n + somatorio(n - 1)


number = 1000000000 # int(input("Digite um numero: "))


def somatorio2(n):
    return ((1 + n) * n) // 2

def somatorio3(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i

    return soma




tempo_inicial = timeit.default_timer()
soma = somatorio2(number)
tempo_final = timeit.default_timer()

print(f"soma = {soma}")
print(tempo_final - tempo_inicial)
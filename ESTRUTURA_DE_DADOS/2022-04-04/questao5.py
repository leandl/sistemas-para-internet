# 5. (Lista) Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os
# armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para
# somar todos os valores digitados.

my_list = []
sun = 0

for _ in range(0, 5):
    new_number = int(input("add number: "))
    my_list.append(new_number)

for number in my_list:
    sun += number

print(sun)
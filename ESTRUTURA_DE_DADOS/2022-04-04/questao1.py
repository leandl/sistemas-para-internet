# 1. Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição,
# subtração, multiplicação e divisão.

number1 = 5
number2 = 6

print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")

if(number2 == 0):
    print("Não é possivel dividir por '0'")
else:
    print(f"{number1} / {number2} = {number1 / number2}")
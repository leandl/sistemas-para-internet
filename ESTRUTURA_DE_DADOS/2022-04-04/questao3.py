# 3. Leia a idade do usuário e classifique-o em:
# - Criança: 0 a 12 anos;
# - Adolescente: 13 a 17 anos;
# - Adulto: acima de 18 anos;
# - Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida.

age = 10

if 0 <= age <= 12:
    print("Criança")
elif 13 <= age <= 17:
    print("dolescente")
elif age >= 18:
    print("aduto")
else:
    print("error")

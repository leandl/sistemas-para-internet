notas = {}
nota_total = 0

for _ in range(0, 3):
    name_aluno = input("Nome do Aluno: ")
    nota_do_aluno = int(input("Nota do Aluno: "))

    notas[name_aluno] = nota_do_aluno


for aluno in notas:
    nota_total += notas[aluno]

media = nota_total / 3

print(f"media = {media}")
class Aluno:
    def __init__(self, name, nota1, nota2):
        self.name = name
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def __str__(self):
        return "name={}, nota1={}, nota2={}".format(self.name, self.nota1, self.nota2)

    def is_aprovado(self):
        return self.media() >= 6



ignacio = Aluno("Ignacio", 3.0, 4)
mateus = Aluno("Mateus", 7.0, 6)


def aluno_aprovado(aluno):
    print(aluno)

    label_status = "APROVADO" if aluno.is_aprovado() else "REPROVADO"
    print(f"{aluno.name} - {label_status}")


aluno_aprovado(ignacio)

aluno_aprovado(mateus)

# class Pessoa:
#     def cumprimentar(self):
#         nome = str(input('Qual seu nome?: '))
#         return f'Olá {nome}'
#
#
# if __name__ == '__main__':
#     p = Pessoa()
#     print(type(p))
#     print(p.cumprimentar())


# Testes

class Humano:
    def __init__(self, nome=None, idade=int, sexo=str):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


humano1 = Humano('Lucas', 28, 'Homem')
humano2 = Humano('Ana', 28, 'Mulher')
humano3 = Humano('Bob', 150, 'Android')

print(humano1.nome)
print(humano2)
print(humano3)

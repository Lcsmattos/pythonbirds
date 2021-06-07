class Pessoa:
    def cumprimentar(self):
        nome = str(input('Qual seu nome?: '))
        return f'Olá {nome}'


if __name__ == '__main__':
    p = Pessoa()
    print(type(p))
    print(p.cumprimentar())

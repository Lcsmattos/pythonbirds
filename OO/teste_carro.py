from unittest import TestCase

from OO.carro import Motor, Direcao


class CarroTestCase(TestCase):
    # Motor
    def teste_velocidade(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        motor.acelerar()
        motor.acelerar()
        motor.frear()
        self.assertEqual(2, motor.velocidade)

    # Direção
    def teste_direcao(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)

    def teste_girar_a_direita(self):
        direcao = Direcao()
        direcao.girar_a_direita()
        self.assertEqual('Leste', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Sul', direcao.valor)

    def teste_girar_a_esquerda(self):
        direcao = Direcao()
        direcao.girar_a_esquerda()
        self.assertEqual('Oeste', direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual('Sul', direcao.valor)


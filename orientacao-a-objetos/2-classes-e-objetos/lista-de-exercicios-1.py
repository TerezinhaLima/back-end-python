# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.



# Crie uma instância da classe carro.


# Faça o carro "andar" utilizando os métodos da sua classe.


# Faça o carro "parar" utilizando os métodos da sua classe.
class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print('O carro foi ligado.')
        else:
            print('O carro já está ligado.')

    def desliga(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print('O carro foi desligado.')
        else:
            print('O carro já está desligado.')

    def acelera(self, quantidade):
        if self.ligado:
            self.velocidade += quantidade
            print(f'O carro acelerou. Velocidade atual: {self.velocidade} km/h')
        else:
            print('O carro precisa estar ligado para acelerar.')

    def desacelera(self, quantidade):
        if self.ligado:
            if self.velocidade >= quantidade:
                self.velocidade -= quantidade
                print(f'O carro desacelerou. Velocidade atual: {self.velocidade} km/h')
            else:
                print('O carro já está parado.')
        else:
            print('O carro precisa estar ligado para desacelerar.')

# Exemplo de uso da classe Carro
meu_carro = Carro(cor='Azul', modelo='Sedan')

meu_carro.liga()
meu_carro.acelera(20)
meu_carro.desacelera(10)
meu_carro.desliga()

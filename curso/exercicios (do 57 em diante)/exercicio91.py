import random
from time import sleep
resultado=list()
jogador=dict()

for c in range(1,5):
    jogador['nome']=str(input(f'Digite o nome do jogador {c}: '))
    jogador['jogada']=random.randint(1,6)
    sleep(1)
    print(f'o jogador {jogador["nome"]} tirou {jogador["jogada"]} no dado!')
    resultado.append(jogador.copy())

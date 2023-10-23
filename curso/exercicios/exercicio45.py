import random
# 1 = tesoura
# 2 = pedra
# 3 = papel
numero=random.randint(1,3)
escolha=str(input("Qual a sua jogada no jogo da pedra papel tesoura? "))
if escolha=="tesoura":
    if numero == 1 :
        print("Empatou")
    elif numero == 2 :
        print("Você perdeu a maquina escolheu pedra. :(")
    elif numero == 3:
        print("Você ganhou!")
elif escolha == "pedra":
    if numero == 1 :
        print("Você ganhou!")
    elif numero == 2 :
        print("Empatou.")
    elif numero == 3:
        print("Você perdeu a maquina escolheu Papel. :(")
elif escolha == "papel":
    if numero == 1 :
        print("Você perdeu a maquina escolheu Tesoura. :(")
    elif numero == 2 :
        print("Você ganhou!.")
    elif numero == 3:
        print("Empatou.")

from random import randint
vitoria=''
while True:
    num=randint(1,3)
    # 1 = Tesoura
    # 2 = Pedra
    # 3 = Papel
    escolha=str(input("Qual sua jogada? [Pedra/Papel/Tesoura] : ")).upper().strip()
    while vitoria!='Perdeu...':
        if escolha == "TESOURA":
            if num == 1 :
                print("Empate!")
                break
            elif num == 2 :
                print("Você perdeu!")
                vitoria = 'Perdeu...'
                break
            elif num == 3 :
                print("Você ganhou!")
        if escolha == "PEDRA" :
            if num == 1 :
                print("Você ganhou!")
            elif num == 2 :
                print("Você empatou!")
                break
            elif num == 3:
                print("Você perdeu!")
                vitoria = 'Perdeu...'
                break
        if escolha == "PAPEL":
            if num == 1:
                print("Você Perdeu!")
                vitoria='Perdeu...'
                break
            elif num == 2 :
                print("Você Ganhou!")
            elif num == 3 :
                print("Você empatou!")
                break
    if vitoria == 'Perdeu...':
        break


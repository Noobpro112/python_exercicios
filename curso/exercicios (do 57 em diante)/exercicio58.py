import random
num = random.randint(1,10)
palpite = 0
jogador = 20
while jogador != num:
    jogador=int(input('Escolha um numero de 1 a 10.'))
    if jogador==num :
        print("Você acertou parabéns!")
        print("Foram necessarios {} palpites!".format(palpite))
    else:
        print('Você errou! :(')
        palpite+=1

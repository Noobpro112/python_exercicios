import random
Jogardor=int(input('Escolha um numero de 1 a 5.'))
num=random.randint(1,5)
if Jogardor==num :
    print("Você acertou parabéns!")
else:
    print('Você errou! :(')

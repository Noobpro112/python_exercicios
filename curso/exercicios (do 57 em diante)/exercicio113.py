def leiaint(msg):
    try:
        n = int(input(msg))
        print(f'Você digitou o número {n}')
    except ValueError:
        print('Tivemos um problema com o valor inteiro digitado.')


def leiafloat(msg):
    try:
        n = float(input(msg))
        print(f'Você digitou o número {n}')
    except ValueError:
        print('Tivemos um problema com o valor float digitado.')

while True:
    n = leiaint('Digite um número inteiro: ')
    n2 = leiafloat('Digite um float: ')

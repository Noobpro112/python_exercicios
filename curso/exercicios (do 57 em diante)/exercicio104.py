def leiaint(msg):
    while True:
        n = str(input(msg)).strip().replace(' ', '')
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[31mERRO: Digite um NÚMERO INTEIRO.\033[m')
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o número inteiro {n}.')
#
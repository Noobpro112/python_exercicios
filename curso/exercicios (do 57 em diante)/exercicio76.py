tupla = ('Aço', 2.50 ,'Ferro', 10 ,'Cobre', 4.5)
while True:
    print('Oque deseja comprar? ')
    print("1 - Aço")
    print("2 - Ferro")
    print("3 - Cobre")
    try:
        escolha=int(input('Digite o numero que deseja: '))
        if escolha == 1:
            escolha-=1
            print(f'Você quer comprar {tupla[escolha]}')
            escolha+=1
            print(f'ele custa {tupla[escolha]} reais')
            break
        elif escolha == 2 :
            print(f'Você quer comprar {tupla[escolha]},')
            escolha+=1
            print(f'e ele custa {tupla[escolha]} reais')
            break
        elif escolha == 3:
            escolha+=1
            print(f'Você quer comprar {tupla[escolha]}')
            escolha+=1
            print(f'e ele custa {tupla[escolha]} reais')
            break
        else:
            print('Invalido.')
    except ValueError:
        print('Invalido')
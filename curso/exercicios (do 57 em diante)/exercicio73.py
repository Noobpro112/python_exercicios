tupla=('Botafogo', 'Grêmio', 'Palmeiras', 'Bragantino', 'Flamengo', 'Atlético-MG', 'Athletico-PR', 'Fluminense', 'São paulo', 'Cuiabá', 'Internacional', 'Santos', 'Corinthians', 'Bahia', 'Vasco', 'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')
while True:
    print('A)Os 5 primeiros colocados da tabela do campeonato brasileiro de futebol.')
    print('B)Os 4 ultimos colocados ta tabela')
    print('C)Uma lista com os times em ordem alfabética')
    print('D)Em que posição está o vasco na tabela?')
    escolha=input("Oque você quer saber: ").upper()
    if escolha=='A':
            print('os 5 primeios são!')
            for time in range(0,5):
                  print(tupla[time])
            break
    if escolha=='B':
        print('Os ultimos 4 times foram')
        for time in range(-4,0):
            print(tupla[time])
        break
    if escolha=='C':
        print('Os times em ordem alfabética fica: ')
        ordem=tuple(sorted(tupla))
        print(ordem)
        break
    if escolha=='D':
        onde=tupla.index('Vasco')
        print(f'Ele está na posição {onde}')
        break
    else:
        print("Opção Invalida")



    
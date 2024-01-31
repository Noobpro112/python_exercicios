lista = []
jogador = {}
gols = []
totgols = 0
totjog = 0
while True:
    totjog += 1
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    jogador['Partidas'] = int(input(f'Quantidade de partidas de {jogador["Nome"]}: '))
    for c in range(0, jogador['Partidas']):
        gols.append(int(input(f'Gols na partida {c + 1}: ')))
        totgols += gols[c]
    jogador['Gols'] = gols[:]
    gols.clear()
    jogador['totgols'] = totgols
    lista.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break
    print('-' * 25)
print('-' * 55)
print('Núm - Nome                - Gols                - Total')
print('-' * 55)
for c in range(0, totjog):
    print(f'{c + 1:<6}', end='')
    print(f'{lista[c]["Nome"]:<22}', end='')
    print(f'{str(lista[c]["Gols"]):<22}', end='')
    print(f'{lista[c]["totgols"]:>5}')
print('-' * 55)
resp = str(input('Deseja mostrar dados de algum jogador? [S/N] ')).strip().upper()[0]
if resp == 'S':
    while True:
        num = int(input('Número do jogador: '))
        print(f'LEVANTAMENTO DO JOGADOR {lista[num - 1]["Nome"].upper()}:')
        for c in range(0, lista[num - 1]["Partidas"]):
            print(f'Jogo {c + 1} => {lista[num - 1]["Gols"][c]} Gol(s)')
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
#
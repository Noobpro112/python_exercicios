jogador = {}
gols = []
total = 0
jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
jogador['Partidas'] = int(input(f'Quantidade de partidas de {jogador["Nome"]}: '))
for c in range(0, jogador['Partidas']):
    gols.append(int(input(f'Gols na partida {c + 1}: ')))
    total += gols[c]
jogador['Gols'] = gols
jogador['Total'] = total
print('-' * 80)
print(jogador)
print('-' * 80)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-' * 80)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for c in range(0, jogador['Partidas']):
    print(f'\t=> Na partida {c + 1} fez {gols[c]} gols.')
print(f'Foi um total de {total} gols.')
#
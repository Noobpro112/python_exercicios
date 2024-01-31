def ficha(n='<desconhecido>', g=0):
    msg = f'O jogador {n} fez {g} gol(s) no campeonato.'
    return msg


nome = str(input('Nome do Jogador: ')).strip().title()
gols = str(input('Número de gols: '))
if nome.isalpha() and gols.isnumeric():
    print(ficha(n=nome, g=gols))
elif nome.isalpha():
    print(ficha(nome, g=0))
elif gols.isnumeric():
    print(ficha(g=gols))
else:
    print(ficha())
#
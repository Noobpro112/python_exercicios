dicio = {}
lista = []
fem = []
acimamedia = []
tot = 0
totidade = 0
while True:
    tot += 1
    dicio['Nome'] = str(input('Nome: ')).strip().title()
    while True:
        dicio['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dicio['Sexo'] == 'F':
            fem.append(dicio['Nome'])
            break
        if dicio['Sexo'] == 'M':
            break
    while True:
        dicio['Idade'] = int(input('Idade: '))
        if dicio['Idade'] > 0:
            lista.append(dicio.copy())
            dicio.clear()
            break
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N' or resp == 'S':
            break
    if resp == 'N':
        break
print('-' * 25)
print(f'Total de pessoas cadastradas: {tot}')
for c in range(0, len(lista)):
    totidade += lista[c]['Idade']
media = totidade // len(lista)
print(f'Média de idade: {media}')
print(f'Mulheres cadastradas: {fem}')
for c in range(0, len(lista)):
    if lista[c]['Idade'] > media:
        acimamedia.append(lista[c]['Nome'])
        acimamedia.append(lista[c]['Idade'])
print(f'Pessoas acima da média de idade: {acimamedia}')
#
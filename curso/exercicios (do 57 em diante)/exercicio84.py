pessoa = list()
dados = list()
quantidade = 0

while True:
    pessoa.append(str(input('Digite o seu nome: ')))
    if pessoa[0] == 'sair':
        break
    pessoa.append(int(input('Digite o seu peso: ')))
    dados.append(pessoa[:])
    pessoa.clear()
    quantidade += 1

dados.sort()

print(f'A pessoa mais pesada tem {dados[-1][1]} kgs, a mais leve tem {dados[0][1]} kgs e foram cadastradas {quantidade} pessoas.')

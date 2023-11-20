pessoa=list()
dados=list()
quantidade=0
while True:
    pessoa.append(str(input('Digite o seu nome: ')))
    if pessoa[0] == 'sair':
        break
    pessoa.append(int(input('Digite o seu peso: ')))
    dados.append(pessoa[:])
    pessoa.clear()
    quantidade+=1
dados.sort()
print('A pessoa mais pesada tem {} kgs a mais leve tem {} kgs e foram cadastradas {} pessoas.'.format(dados[-1,1], dados[0,1], quantidade))
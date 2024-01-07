escola=list()
aluno=dict()
aluno['nome']=str(input('Digite o nome do aluno: '))
aluno['média']=float(input(f'Digite a média do {aluno["nome"]}: '))
print(f'O nome do aluno é {aluno["nome"]}')
print(f'Sua média foi de {aluno["média"]}')
if aluno['média']>=7.0:
    print(f'A situação do aluno é Aprovada!')
else:
    print(f'A situação do aluno é Reprovada!')


locadora=list()
filme=dict()
for c in range(0,3):
    filme['Titulo']=str(input('Digite o titulo do filme: '))
    filme['Ano']=int(input('Digite o ano de lançamento do filme: '))
    locadora.append(filme.copy())
print(locadora)

for e in locadora:
    for k,v in e.items():
        print(f'o campo {k} tem valor {v}.')
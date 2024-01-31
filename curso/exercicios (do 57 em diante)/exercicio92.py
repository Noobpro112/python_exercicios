from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de Nascimento: '))
dados['Idade'] = date.today().year - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho [0 não tem]: '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Contratação'] + 35 - nascimento
print('-' * 35)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
#
from package.exercicio115 import *
from time import sleep
import os


arq = 'lista.txt'
if not arqexiste(arq):
    criararq(arq)



while True:
    resposta = menu(['Ver Pessoas cadastradas',' Cadastrar nova Pessoa', ' Sair do sistema'])
    if resposta == 1:
        lerarq(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('ERRO! Tente novamente.')
    sleep(2)

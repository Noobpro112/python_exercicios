import os


def lerarq(nome):
    try:
        with open(nome, 'rt') as arquivo:
            cabecalho('Pessoas Cadastradas')
            print(f'{"Nome":<30}{"Idade":<12}')
            print('-' * 42)
            for linha in arquivo:
                nome, idade = linha.strip().split(';')
                print(f'{nome:<30}{idade:<12}')
    except Exception as e:
        print(f'Problema ao ler o arquivo: {e}')
    finally:
        arquivo.close()




def arqexiste(nome):
    return os.path.exists(nome)


def criararq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um erro com a criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            return n  
        except ValueError:
            print("Por favor, digite um número inteiro válido.")


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc

def cadastrar(arq,nome = 'Desconhecido',idade= '0'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo! ')
    else:
        try:
            a.write(f'{nome};{idade} Anos\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print('Novo registro adicionado.')

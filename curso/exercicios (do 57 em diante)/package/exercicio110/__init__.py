def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor}'
def aumentar(valor=0,taxa_maior=0, formato=False):
    valor=valor+(valor*taxa_maior/100)
    return valor if formato == False else moeda(valor)
def diminuir(valor=0,taxa_menor=0, formato=False):
    valor=valor-(valor*taxa_menor/100)
    return valor if formato == False else moeda(valor)
def dobro(valor=0, formato=False):
    valor*=2
    return valor if formato == False else moeda(valor)
def metade(valor=0, formato=False):
    valor/=2
    return valor if formato == False else moeda(valor)
def resumo(valor,taxa_maior,taxa_menor):
    print('--'*10)
    print('Resumo!')
    print('--'*10)
    print(f'Aumentando em {taxa_maior}%, o número {moeda(valor)} fica {(aumentar(valor,taxa_maior, True))}')
    print(f'Diminuindo em {taxa_menor}%, o número {moeda(valor)} fica {(diminuir(valor,taxa_menor, True))}')
    print(f'O dobro do número {moeda(valor)} fica {(dobro(valor, True))}')
    print(f'A metade do número {moeda(valor)} fica {(metade(valor, True))}')
    print('--'*20)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor}'
def aumentar(valor=0, formato=False):
    valor=valor+(valor*10/100)
    return valor if formato == False else moeda(valor)
def diminuir(valor=0, formato=False):
    valor=valor-(valor*13/100)
    return valor if formato == False else moeda(valor)
def dobro(valor=0, formato=False):
    valor*=2
    return valor if formato == False else moeda(valor)
def metade(valor=0, formato=False):
    valor/=2
    return valor if formato == False else moeda(valor)
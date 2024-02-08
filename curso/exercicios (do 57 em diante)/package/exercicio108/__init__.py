def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor}'
def aumentar(valor=0, moeda='R$'):
    valor=valor+(valor*10/100)
    return valor
def diminuir(valor=0, moeda='R$'):
    valor=valor-(valor*13/100)
    return valor
def dobro(valor=0, moeda='R$'):
    valor*=2
    return valor
def metade(valor=0, moeda='R$'):
    valor/=2
    return valor
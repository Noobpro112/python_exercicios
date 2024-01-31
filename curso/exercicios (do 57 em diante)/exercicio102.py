def fatorial(n=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: Número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de n.
    """
    print('-' * (n * 5))
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c == 1:
                print(' = ', end='')
            else:
                print(' x ', end='')
    return f


n = int(input('Fatorial: '))
resp = str(input('Mostrar [S/N]: ')).strip().lower()[0]
if n < 1:
    print('ERRO: Fatorial deve ser maior que 0.')
else:
    if resp == 's':
        show = True
    else:
        show = False
    print(fatorial(n, show))
#
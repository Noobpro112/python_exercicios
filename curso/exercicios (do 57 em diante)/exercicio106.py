c = ('\033[m',
     '\033[41m',
     '\033[42m',
     '\033[43m',
     '\033[44m',
     '\033[45m',
     '\033[7m',
     )

def ajuda(com):
    titulo(f"MANUAL DO COMANDO '{com}'", 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
#
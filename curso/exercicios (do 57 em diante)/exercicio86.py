matriz=[[ 0, 0, 0],[ 0, 0, 0],[ 0, 0, 0]]
soma=terceira_coluna=0
for l in range(0,3):
    for c in range(0,3) :
        matriz[l][c]=int(input(f'Digite um valor de [{l}][{c}]: '))

print('-='*30)
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()
print('-='*30)

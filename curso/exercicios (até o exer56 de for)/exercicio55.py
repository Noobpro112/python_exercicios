maior_peso = 0
menor_peso = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa (em kg): '))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print('O maior peso lido foi de {}kg'.format(maior_peso))
print('O menor peso lido foi de {}kg'.format(menor_peso))

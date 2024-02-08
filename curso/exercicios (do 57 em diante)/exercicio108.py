import package.exercicio108 as moeda

num = float(input('Digite um valor: '))

print(f'Aumentando em 10%, o número {moeda.moeda(num)} fica {moeda.moeda(moeda.aumentar(num))}')
print(f'Diminuindo em 13%, o número {moeda.moeda(num)} fica {moeda.moeda(moeda.diminuir(num))}')
print(f'O dobro do número {moeda.moeda(num)} fica {moeda.moeda(moeda.dobro(num))}')
print(f'A metade do número {moeda.moeda(num)} fica {moeda.moeda(moeda.metade(num))}')

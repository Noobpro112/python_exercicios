import package.exercicio109 as moeda

num = float(input('Digite um valor: '))

print(f'Aumentando em 10%, o número {moeda.moeda(num)} fica {(moeda.aumentar(num, True))}')
print(f'Diminuindo em 13%, o número {moeda.moeda(num)} fica {(moeda.diminuir(num, True))}')
print(f'O dobro do número {moeda.moeda(num)} fica {(moeda.dobro(num, True))}')
print(f'A metade do número {moeda.moeda(num)} fica {(moeda.metade(num))}')

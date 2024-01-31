def maior(*numeros):
    print('')
    print('Analisando dados!')
    print('~~~~'*8)
    lista=numeross[:]
    lista.sort()
    print(f'o maior é {lista[-1]}')
    print('~~~~'*8)
numeross=list()
quantos = int(input('Quantos numeros deseja colocar: '))
if quantos <= 0:
    print('Não é possivel analisar.')
while quantos >0:
    num=int(input('Digite um numero: '))
    quantos-=1
    numeross.append(num)
maior(numeross)
#
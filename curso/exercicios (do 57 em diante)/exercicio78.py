lista=[int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: '))]

lista.sort()
menor=lista[0]
maior=lista[-1]

print('Você digitou os seguintes numeros: {}, Seu menor numero é {} e o maior é {}'.format(lista,menor,maior))
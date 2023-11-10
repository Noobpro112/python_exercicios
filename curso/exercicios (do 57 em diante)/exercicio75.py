tupla=(int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')))
try:
   
    indice = tupla.index(3)
except ValueError:
    print("O número 3 não está na tupla.")
quantos_9=tupla.count(9)
numeros_pares=0
if tupla[0] % 2 ==0:
    numeros_pares+=1
if tupla[1] % 2 ==0:
    numeros_pares+=1
if tupla[2] % 2 ==0:
    numeros_pares+=1
if tupla[3] % 2 ==0:
    numeros_pares+=1
print(f'O valor 9 apareceu {quantos_9} vezes o numero 3 apareceu a primeira vem em {indice} e tem {numeros_pares} numeros pares. ')


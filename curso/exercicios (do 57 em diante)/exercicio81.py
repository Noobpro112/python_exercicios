lista=[]
quantidade=0
while True:
    quantos=int(input('Quantos numeros você quer digitar: '))
    while quantos>=1:
        num=int(input("Digite um numero: "))
        lista.append(num)
        quantidade+=1
        quantos-=1
    quantos=int(input('Digite mais um numero caso queira continuar digitando: '))
    lista.sort(reverse=True)
    quantos_5=lista.count(5)
    print(f'Foram digitados {quantidade} e o numero 5 apareceu {quantos_5} vezes  e sua lista ficou assim: {lista} em ordem decrescente.')
    break

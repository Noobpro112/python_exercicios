Lista=[]
lista_par=[]
lista_impar=[]
while True:
    num=int(input("Digite um numero: "))
    Lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    escolha=str(input("Quer continuar? Y/N")).upper()
    if escolha == 'N':
        break
    elif escolha == 'Y':
        print('Ok')
    else:
        print('Incorreto.')
        break
print(f'A sua lista ficou assim: {Lista}, os numeros pares são {lista_par} e os numeros impars são {lista_impar}.')
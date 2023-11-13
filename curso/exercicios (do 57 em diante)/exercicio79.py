lista=[]
while True:
    num=int(input('Digite um numero: '))
    achar=lista.count(num)
    if achar==1:
        print('Numero já digitado!')
    else:
        lista.append(num)
    escolha=str(input("Deseja continuar? Y/N ")).capitalize()
    if escolha == 'N':
        lista.sort()
        print('Essa é sua lista: ', lista)
        break
    elif escolha == 'Y':
        print('Ok')
    else:
        print('Erro')
print('Finalizado.')

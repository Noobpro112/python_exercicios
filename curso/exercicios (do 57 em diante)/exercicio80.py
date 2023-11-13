lista=[]
num=int(input('Digite Um numero: '))
lista.append(num)
menor_numero=num
maior_numero=num
for i in range(1,5):
    num=int(input('Digite Um numero: '))
    if num<menor_numero:
        lista.insert(0,num)
    elif num>maior_numero:
        lista.append(num)
    elif num>lista[1]:
        lista.insert(2,num)
    elif num>lista[2]:
        lista.insert(3,num)
    elif num>lista[3]:
        lista.insert(4,num)
    elif num<lista[2]:
        lista.insert(1,num)
    elif num<lista[3]:
        lista.insert(2,num)
    elif num<lista[4]:
        lista.insert(3,num)
print('Acabou')
print(lista)


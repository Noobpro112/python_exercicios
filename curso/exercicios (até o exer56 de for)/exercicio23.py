num=str(input('Escolha um numero de 0 a 9999: '))
num1='0000'+num
dividir = num1.replace('', ' ')
lista = dividir.split()
print(lista)
unidade, decimal, centena, milhar=lista[-1], lista[-2], lista[-3], lista[-4]
print('A unidade é {}, o seu decimal é {}, a sua centena é {} e seu milhar é {}'.format(unidade,decimal,centena,milhar))

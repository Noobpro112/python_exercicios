numeros=list()
par=list()
impar=list()
c=0
for i in range(1,8):
    num=int(input(f'Digite o seu {i} numero: '))
    numeros.append(num)
for i in range(0,7):
    if numeros[c] % 2 == 0 :
        par.append(numeros[:][c])
    else:
        impar.append(numeros[:][c])
    c+=1
par.sort()
impar.sort()
print('-='*30)
print(f'Sua lista par ficou assim! {par}')
print(f'Sua lista impar ficou assim! {impar}')
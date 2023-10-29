km=float(input('Quantos kilometros o carro andou a sua posse? '))
dias=int(input('Quantos dias vocês ficaram com o carro?'))
kmr=km*0.15
diasr=dias*60
total=(kmr+diasr)
print ('O valor total de suas viagens é R${}'.format (total))
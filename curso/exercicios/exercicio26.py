frase=str(input('Digite uma frase! ')).upper()
frase1=frase.strip()
print('A letra A apareçe {} vezes'.format(frase1.count('A')))
print('A letra A apareçe na casa {} pela primeira vez'.format(frase1.find('A')+1))
print('A letra A apareçeu pela ultima vez na casa {}. '.format(frase1.rfind('A')))

#o find acha a primeira vez que a letra apareceu
#o rfind começa pelo lado direito ou seja de tras para frente
frase=str(input('Digite uma frase! ')).upper().strip()
print('A letra A apareçe {} vezes'.format(frase.count('A')))
print('A letra A apareçe na casa {} pela primeira vez'.format(frase.find('A')+1))
print('A letra A apareçeu pela ultima vez na casa {}. '.format(frase.rfind('A')))

#o find acha a primeira vez que a letra apareceu
#o rfind começa pelo lado direito ou seja de tras para frente
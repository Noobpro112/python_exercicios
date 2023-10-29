dias=int(input('Quantos dias tem o ano atual? '))
if dias == 365 :
    print('O ano não é bissexto')
elif dias == 366 :
    print('O ano é bissexto')
else:
    print('Ensira uma data valida para o programa.')
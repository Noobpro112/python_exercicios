km = int(input('Quantos KM vc vai rodar?'))
if km<=200:
    print('o valor da viagem será {}'.formart(km*0.45))
else:
    print('O calor da viagem será {}'.format(km*0.5))
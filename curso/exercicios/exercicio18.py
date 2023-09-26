import math
angulo = float(input('Digite o angulo que você deseja.'))
seno=math.sin(math.radians(angulo))
print('o Angulo tem de {} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno=math.cos(math.radians(angulo))
print ('O Ângulo tem de {} tem o COSSENO de {}'.format (angulo , cosseno ))
tangente=math.tan(math.radians(angulo))
print('{} tem a TANGENTE de {:.2f} '.format(angulo, tangente) )
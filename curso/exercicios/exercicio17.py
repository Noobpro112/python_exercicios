import math
co=int(input("Qual o seu cateto oposto?"))
catad=int(input("Qual o seu cateto adjacente?"))
hipotenusa=(co**2+catad**2)
h=math.sqrt(hipotenusa)
print('A hipotenusa vai medir {:.1f}'.format(h))
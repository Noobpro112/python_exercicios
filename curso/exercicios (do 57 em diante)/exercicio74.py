from random import randint
tupla=(randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print(f'Sua listagem de numeros é {tupla}')
tupla_maior=max(tupla)
tupla_menor=min(tupla)
print(f"Seu menor numero de sua tupla é {tupla_menor} e a maior é {tupla_maior}")
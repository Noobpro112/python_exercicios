import random
numeros=list()
par=0

def sorteia():
    for c in range(0,5):
        num=random.randint(0,10)
        numeros.append(num)
        somaPar(num)
        num=0
        print(numeros)
def somaPar(num):
    if num % 2 == 0:
        global par
        par+=num


sorteia()
print("Soma dos números pares:", par)
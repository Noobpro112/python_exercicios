num=0
soma=0
quantos=0
while num!=999:
    num=int(input("Escolha um numero! "))
    if num!=999:
        soma+=num
        quantos+=1
print("Você digitou {} sua soma são {}!".format(quantos,soma))
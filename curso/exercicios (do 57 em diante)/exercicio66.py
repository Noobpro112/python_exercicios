num=0
soma=0
quantos=0
while True:
    num=int(input("Escolha um numero! "))
    soma+=num
    quantos+=1
    if num== 999:
        break
print(f"Você digitou {quantos-1} sua soma são {soma-999}!")
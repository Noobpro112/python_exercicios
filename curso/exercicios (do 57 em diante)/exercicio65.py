quantos=int(input("Quantos numeros você quer calcular? "))
num_media=0
soma=0
while quantos >= 1 :
    while quantos>=1 :
        num=float(input("Digite seu numero: "))
        num_media+=1
        soma+=num
        quantos-=1
    media=soma/num_media
    print("Sua média de todos os numeros são {} e a soma de todos os numeros são {} ".format(media,soma))
    quantos=int(input("Você quer colocar mais numeros? "))
    if quantos == 0 :
        break
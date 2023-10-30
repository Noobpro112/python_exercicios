vezes=0
while True:
    num=int(input("Digite um numero para efetuar a tabuada: "))
    while vezes < 10:
        if num < 0 :
            break
        vezes+=1
        multi=num*vezes
        print(f"Sua multiplicação de {num} x {vezes} é {multi}. ")
    
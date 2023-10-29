print("Vamos ver uma Razão aritmétria")
r=int(input("Qual a sua razão? "))
a1=int(input("Qual o seu primeiro termo? "))
c=int(input("Quantos termos você quer? "))
while True:
    while c >1 :
        if c == 0:
            print("Adeus Não existe PA!")
            pass
        an =a1+(c - 1)*r
        c-=1
        print("A sequencia de numeros de sua PA pela quantidade de termos escolhidos por você é : {}".format(an))
    escolha = str(input("Quer mostrar mais termos? [Y/N]")).upper()
    if escolha == "Y":
        c=int(input("Mais quantas vezes?"))
        if c == 0:
            print("Adeus Não existe PA!")
            pass
    if escolha=="N":
        pass
    pass
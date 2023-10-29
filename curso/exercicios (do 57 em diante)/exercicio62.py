print("Vamos ver uma Razão aritmétria")
r=int(input("Qual a sua razão? "))
a1=int(input("Qual o seu primeiro termo? "))
c=int(input("Quantos termos você quer? "))
c1=c
while c>1:
    while c >1 :
        an =a1+(c - 1)*r
        if c1==c:
            an_quantidade=an    
        c-=1
        print("A sequencia de numeros de sua PA pela quantidade de termos escolhidos por você é : {}".format(an))
    escolha = str(input("Quer mostrar mais termos? [Y/N]")).upper()
    if escolha == "Y":
        c=int(input("Mais quantas vezes?"))
        a1=an_quantidade
        pass
    if escolha=="N":
        break

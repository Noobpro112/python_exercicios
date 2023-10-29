print("Vamos ver uma Razão aritmétria")
r=int(input("Qual a sua razão? "))
a1=int(input("Qual o seu primeiro termo? "))
c=int(input("Quantos termos você quer? "))
while c >1 :
    if c == 0:
        print("Adeus Não existe PA!")
        break
    an =a1+(c - 1)*r
    c-=1
    print("A sequencia de numeros de sua PA pela quantidade de termos escolhidos por você é : {}".format(an))
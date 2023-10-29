print("Vamos ver uma Razão aritmétria")
r=int(input("Qual a sua razão? "))
a1=int(input("Qual o seu primeiro termo? "))
c=10
while c >1 :
    an =a1+(c - 1)*r
    c-=1
    print("A sua progressão aritmétrica é : {}".format(an))
print("Sua PA é essa!")
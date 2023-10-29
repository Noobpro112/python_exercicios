print("Vamos ver uma Razão aritmétria")
r=int(input("Qual a sua razão?"))
a1=int(input("Qual o seu primeiro termo?"))
for c in range(1,11):
    an =a1+(c - 1)*r
    print("A sua progressão aritmétrica é : {}".format(an))
print("Sua PA é essa!")
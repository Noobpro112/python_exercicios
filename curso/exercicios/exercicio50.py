soma = 0 
for i in range(1,7):
    n=int(input("Escolha seu {}° numero! ".format(i)))
    if n % 2 == 0:
        soma += n
print(soma)


"""numeros = []
soma = 0
for l in range(1, 7):
    n = int(input("Escolha seu {} numero.".format(l)))
    numeros.append(n)
    if n % 2 == 0:
        soma += n
print(soma)
"""

#O .append coloca tudo que foi colocado na variavel "n" em for em uma lista. (usar o append é mais daorinha, mas ele não ensinou XD)
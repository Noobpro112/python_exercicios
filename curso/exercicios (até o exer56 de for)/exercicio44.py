produto=float(input("Qual o preço do produto? "))
forma_de_pagamento=str(input("Qual a forma de pagamento?"))
if forma_de_pagamento=="Cartão":
    vezes=int(input("Em quantas vezes?"))
    if vezes == 2:
        desconto=produto*5/100
        preco=produto-desconto
        print("Você deve pagar ${}".format(preco))
    elif vezes == 3:
        print("Você deve pagar ${}".format(produto))
    elif vezes == 4 :
        juros=produto*20/100
        preco=produto-juros
        print("Você deve pagar ${}".format(preco))
elif forma_de_pagamento=="dinheiro" or "Dinheiro":
    desconto=produto*10/100
    preco=produto-desconto
    print("Você deve pagar ${}".format(preco))

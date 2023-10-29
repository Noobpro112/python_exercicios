print("Calculadora de idade!")
for i in range(1,7):
    ano=int(input("Em que ano você nasceu?"))
    if ano == 2005:
        mes=int(input("Em que mês você nasceu?"))
        if mes>5:
            print("Não tem mais de 18 anos de idade!")
        else:   
            print("Tem mais de 18 anos!")
    elif ano<2005:
        print("Tem mais de 18 anos")
    else:
        print("Não tem mais de 18 anos de idade!")
print("Acabou!")






#data de hoje 27/10/2023
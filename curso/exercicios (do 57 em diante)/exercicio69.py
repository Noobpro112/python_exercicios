idade=0
sexo=''
quantidade_sexo_m=0
quantidade_mulher_20=0
quantidade_18=0

while True:
    idade=(input("Digite sua idade: "))
    if idade.isnumeric():
        idade = int(idade)
        sexo=str(input("Digite seu sexo: [M/F] ")).upper()
        if idade>=18 :
            quantidade_18+=1
        if sexo == 'M' :
            quantidade_sexo_m+=1
        if sexo == 'F' :
            if idade <= 20:
                quantidade_mulher_20+=1
        if sexo != 'M' and sexo != 'F' and sexo!='SAIR':
            print("Opção invalida!")
        if sexo == 'SAIR':
            break
    else:
        print("Opção invalida!")
    

if sexo == 'SAIR':
    print("A quantidade de homens que compareceram foi {} a quantidade de mulheres a baixo de 20 anos foi {} e a quantidade de pessoas maiores de 18 anos foi {}".format(quantidade_sexo_m,quantidade_mulher_20,quantidade_18))
  

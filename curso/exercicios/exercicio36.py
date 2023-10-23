Casa=int(input("Qual o valor da casa?"))
Salario=float(input("Qual a sua renda mensal?"))
tempo=int(input("Quantos anos você pretende pagar?"))
tirar_do_salario=(Salario * 30/100)
salario1=Salario-tirar_do_salario
Necessario_para_pagar=Casa/(tempo*12)
if(Necessario_para_pagar>=salario1):
    print("Você não pode comprar")
    print(Necessario_para_pagar, salario1)
else :
    print("Pode comprar")
    print(Necessario_para_pagar, salario1)


"""O exercicio em questão era para calcular o salario do cara e a prestação mensal não poderia passar de 30% do 
salario, eu acho que ta certo."""
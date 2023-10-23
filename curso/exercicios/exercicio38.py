num1=int(input("Qual seu primeiro numero? "))
num2=int(input("Qual o seu segundo numero? "))

if num1==num2:
    print("Os dois numeros são iguais.")
elif num2>num1:
    print("O Numero {} é maior que o numero {}".format(num2,num1))
elif num1>num2:
    print("O Numero {} é maior que o numero {}".format(num1,num2))
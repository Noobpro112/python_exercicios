nota1=float(input("Qual sua primeira nota?"))
nota2=float(input("Qual sua segunda nota?"))
média=(nota1+nota2)/2
if média>=7.0:
    print("Aprovado")
elif média<5.0:
    print("Reprovado")
else:
    print("Recuperação")
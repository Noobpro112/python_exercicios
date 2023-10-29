n1 = int(input("Escolha um número para calcular o fatorial: "))
fatorial_resultado = 1
fatorial = n1

while fatorial > 1:
    fatorial_resultado *= fatorial
    fatorial -= 1

print("O resultado da sua fatorial é {}".format(fatorial_resultado))    

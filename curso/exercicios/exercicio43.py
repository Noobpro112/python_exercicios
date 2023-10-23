peso = int(input("Quantos quilogramas você pesa?"))
altura_cm = int(input("Quantos centímetros você mede?"))

altura_m = altura_cm / 100

imc = peso / (altura_m ** 2)

print("Seu IMC é:", imc)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Peso ideal")
elif imc < 29.9:
    print("Você está com sobrepeso.")
elif imc < 39.9:
    print("Você está obeso.")
else:
    print("Você está com obesidade mórbida.")

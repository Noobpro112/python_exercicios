frase=str(input("Sua palavra é um palindromo? "))
frase1=frase.replace(" ","").lower()
if frase1 == frase1[::-1]:
    print("É Um palindromo.")
else:
    print("Não é um palindromo")
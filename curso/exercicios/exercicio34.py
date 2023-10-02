sal=float(input('Quanto você ganha?'))
if sal>=1250.0:
    print ('Seu aumento é de 10%')
    aumento=sal+(sal*10/100)
    print(aumento)
else:
    print ('Seu aumento é de 15%')
    aumento=sal+sal*(15/100)
    print(aumento)
h_idade_maior = 0
h_nome_maior = ""
mulher_menos_20 = 0
media_idade=0
for i in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa : '.format(i))).strip()
    idade = int(input("Qual a idade da {}º pessoa: ".format(i)))
    sexo=str(input("Digite o sexo da {}º pessoa: ".format(i))).strip()
    #Idade das mulheres
    if sexo == "mulher" :
        if idade <=20:
            mulher_menos_20+=1
    #Nome do homen mais velho
    if sexo == "homen" :
        if i == 1:
            h_idade_maior = idade
            h_nome_maior=nome
        else:
            if idade > h_idade_maior:
                h_idade_maior = idade
                h_nome_maior = nome
    #Média das idades.
    media_idade+=idade
media=media_idade/4
print("A média de idade dos participantes são: {} anos".format(media))
print("A quantidade de mulheres com menos de 20 anos são: {}".format(mulher_menos_20))
print("O homem mais velho é: {} ".format(h_nome_maior))
#primeira vez que eu usei comentario efetivamente para a coompreensão do programa (isso não foi feito por chat GPT.)
nome = input('Qual seu nome? ')
nome_s = len(nome.replace(' ', ''))
nome_s_d=nome.split()
print(nome_s_d)
nome_s_d_1=len(nome_s_d[0])
print(""" 
Seu nome em maiusculo é {}
Seu nome em minusculo é {}
A quantidade de caracteres que seu nome tem é {}
A quantidades de caracteres do seu primeiro nome é{}""".format(nome.upper(),nome.lower(),nome_s,nome_s_d_1))
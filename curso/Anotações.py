# Adição == +
# Subtração == -
# Multiplicação == *
# Divisão == /
# Potência == **
# Módulo/resto da divisão == %
# Divisão Inteira == //

# Todos necessitam de um operando. (numero ou texto ou seja, string, ou int.)

# Igualdade é feito por ==. 
# o = é feito por RECEBE.

# vamos testar:
#print(5+2)
#print(10-3)
#print(4*6) # multiplicaçao
#print(2**7)# potenciação tambem pode ser feita pelo comando pow(), EX: pow(4,3) resultado será 64.
#print(5%2) # modulo, seria o depois da virgula de uma divisão inteira.
#print(89//10) # Numero não ficara em float. ele vai ficar com o maximo que seria possivel dividir antes de colocar a virgula.

# Ordem de precedencia (quem deve ser execultado primeiro!)
# ()
# **
# * , / , // , %
# + , -

#caso queria quebrar uma linha no meio de um print basta colocar \n (sim barra ao contrario) e caso não queira quebrar a linha de uma print para outra basta colocar end='' no final, EX:
nome = 'a'
print('o armario do {} está dessarumado'.format(nome), end=' ')
print('e agora está de castigo.')
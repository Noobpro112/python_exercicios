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
"""nome = 'a'
print('o armario do {} está desarumado'.format(nome), end=' ')
print('e agora está de castigo.')"""

#Modulos, normalmente utilizados no começo de um codigo em python
# Modulos são tipo "DLCS" de comandos para o python.
# normalmente representado pelo comando : import "nome do módulo" mas importa o modulo INTEIRO.
# tambem pode pegar algo especifico e não ele todo ex : from "nome do módulo" import "comando"
#comando real:
# import math
# ele tem as funcionalidades:
#ceil: arredonda para cima
#floor: arredonda para baixo
#trunc:elimina os numeros depois da virgula
#pow:exponencial
#sqrt:Raiz quadrada
#factorial:


#Manipulação de texto:

#fatiamento de string, como por exemplo
#len()
#count()
#find()
#replace()
#upper(): tudo maiusculo
#lower():tudo minusculo
#capitalize():primeira letra maiuscula restante minusculas
#title():todas palavras iniciadas pela Maiúscula
#strip():remove espaços antes ou após a string
#lstrip(): remove apenas espaços antes da string
#rstrip(): remove somente espaços após a string
#split(): separa a string em partes que estão entre parênteses
#join(): junta strings dentro de outra string          EX:           depois de um split deve usar o           '-'.join(frase)
#format(): formata valores dentro das chaves


#len(frase) mostra o tamanho/quantidade de caracteres em uma frase
#frase.count('o') conta quantos 'o' tem em uma frase, apenas o 'o' o 'O' não está incluido
#o fatiamento pode ser utilizado com esse codigo, ex: frase.count('o',0.13)
#o fatiamento normal ocorre como frase=[0:21:2]    0= começo                21= final/termino                2= quantas casas ele vai pulando.
#A frase já deveria estar definida como "Frase='Meu amigo é o python'"
#frase.find('amigo') encontra onde esta escrito 'amigo' na variavel Frase, caso não exista ele vai te retornar o valor '-1' ou seja não encontrado.
#o find acha a primeira vez que a letra apareceu
#o rfind começa pelo lado direito ou seja de tras para frente
# pode ser utilizado ('curso' in frase) ele te retornar como True ou False. para dizer se tem ou não, (operador, ele não é um comando.)
#frase.replace('amigo','inimigo') autoexplicativo, ele substituie na frase.

#Print com aspas tripla coloca TUDO em comentario

"""
Laços de Repetição (For):

Em portugues um exemplo seria:

Laço c no intervalo(1,10):           OBS: C é uma variavel; Pode ser chamada de como quiser.
    passo
pega

Obs: veja que o "pega" está fora do laço já que ficou fora da identação! Logo ele repete tudo que estiver dentro dele por identação.

Em python agora fica.

for c in range(1,10):
    passo
pega

(Lembrando que o 1 é 0...)

É possivel usar if e else em laço for. ou seja

for i range(0,1):
    if rafael=="Amigo":
        print("Amigo estou aqui!")
    else:
        print("O seus problemas, São meus Tambem!")
print("Toy Story Referency")

(Sempre prestando atenção na identação.)

Se quiser contrar ao contrario basta colocar -1 no numero que deseja chegar ou seja 
for c in range(10, 0, -1): (Isso conta de trás para frente.) 
e isso serve para contar de numero de 2 em 2 ou de 5 em 5 tanto faz, basta mudar o numero.
"""

"""
Laço de repetiçao (While)

While pode ser definido em português como "enquanto" 

ou seja, enquanto não chegue a isso ou enquanto não tenha isso faça:

EX:

enquanto não (objeto/algo):
    faça isso

Em python ficaria:

while not (object/something)
    do this.

Tupla:

mais valores para apenas uma variavel.
Ou seja, Variavel composta.
Tem 3 maneiras de fazer as variaveis composta, sendo elas
Tupla
Lista
Dicionario

Agora falaremos da Tupla

Suponhamos que temos uma variavel lanche com 4 variaveis
lanche = (hamburgue, Suco, Pizza, Pudim)

cada valor é um "numero" ou seja o 0 sera o "hamburgue" o 1 o "suco" e assim pro diante.

se fizermos um print(lanche) ele vai printar TUDO
se fizer um print(lanche[2]) ele vai printar a pizza.
se fizer uma print(lanche[0:2]) ele vai printar o hamburgue e o suco, excluindo o 2 que seria a pizza.
se fizer uma print(lanche[1:]) ele vai excluir o hamburgue e printar o resto.
podemos usar também o comando (len) que vai mostrar a quantidade de valores dentro de uma variavel.

vamos fazer um for.

for comida in lanche:
    print(f'Eu vou comer {comida}. )
print("Comi pra caramba")

ele vai printando cada valor fazendo a variavel comida uma variavel simples.

AS TUPLAS SÃO IMUTÁVEIS ou seja, elas não mudam. é impossivel tirar um pudim da tupla. você não consegue mudar a tupla dentro do programa, apenas no codigo fora da execução.


podemos ver a tupla funcionando com outro for que seria:

for cont in range(0, len(lanche)):
    print(lanche[cont])
print("Muita comida")


tem a maneira do enumerate tb.

for posicao, comida in enumarate(lanche):
    print(f'nome da comida na posição {posicao} é {comida})

da pra usar tb outros comandos dentro de tupla como o

.index()

exemplo

print(lanche.index('algo')) ele vai falar aonde o "algo" está, em que posição.







"""
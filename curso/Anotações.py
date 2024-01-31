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

//////////////////////////////////////////////////////////////////////////////////////    

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
.count() conta quantas vezes algo apareceu.

exemplo

print(lanche.index('algo')) ele vai falar aonde o "algo" está, em que posição.

///////////////////////////////////////////////////////////////

Lista:

Aula 1 - 

uma lista é usada colchetes []

lanche = ['Hamburguer','suco','pizza','pudim']

elas são mutaveis, ou seja elas mudam.

se colocar lanche[3]='sorvete'
o pudim virou o sorvete agora.


para adicionar coisas na lista, extra em vez de mudar deve usar o comando .append('')
ou seja ele cria um valor a mais

existe o .insert(0,'')
ele adiciona algo em um lugar especifico.

para excluir algo podemos usar o "del" ou o .pop(local) ou .remove('valor')
EX:

del lanche[3]
lanche.pop(3)
lanche.remove('pizza')

se não tiver algo dentro do .pop ele remove o ultimo item da lista.

se quisermos saber se tem um valor especifico em uma lista podemos usar o if com o in ou seja :

if 'pizza' in lanche:
    lanche.remove('pizza')

pode se criar lista com o range 

EX:

valores=list(range(4,11))

e vai ficar 

valores=[4,5,6,7,8,9,10]

.sort() utilizado para deixar em ordem numérica.
.sort(reverse=True) ordenado em ordem reversa.

len(valores) mostra a quantidade de valores dentro de uma lista.

ao criar uma lista e igualar a outra lista, elá cria uma ligação ou seja, se uma for mudada a outra tb muda.

se quiser fazer uma copia vc deve fazer isso:

a=['cavalo','bolsa']
b=a[:]
b[1]= 'Bolsa' 

pronto, vc fatia e fala que ele deve receber todos os numeros de A em vez de fazer uma ligação

adicionar lista dentro de listas.

dados=['rafael', 25]
pessoas=[]
pessoas.append(dados)

vai ficar 

pessoas[['rafael', 25],]

print(pessoas[0][0])

vai sair 'rafael'

to buscando algo dentro de uma lista dentro de outra lista.

vai adicionando os dados em laço for ou while pra ir adicionando de uma forma mais "rapida"


EX:

galera=list()
dado=list()
for c in range(0,3):
    dado.append(str(input('Nome: )))
    dado.append(int(input('Idade: )))
    galera.append(dado[:])
    dado.clear()
prit(galera)


/////////////////////////////////////////////


Dicionario:

os dicionarios são indentificados pelas chaves {}

ou seja:

suponhamos que temos umalista chamada dados

dados=list()

contendo Pedro no indice 0 e 25 no indcice 1

ai eu defino como um dicionario

dados=dict()
ou
dados={}

então podemos fazer a seguinte coisa:

dados={'nome': Pedro, 'Idade': 25}

e podemos printar da seguinte forma:
print(dados['nome']) e vai sair "Pedro"

caso queira adiconar um novo indice nesse dicionario o append não ira funcionar.

então caso vc queira colocar por exemplo o sexo do pedro, basta fazer isso:


dados['sexo']='M'

pronto, por ser um dicionario ele ficara dessa forma.

caso queira remover basta usar o del ou seja,

del dados['sexo']

podemos fazer um dicionario da seguinte forma tb:

filme= { 'Titulo' : 'Star Wars',
    'Ano':1977,
    'Diretor': 'George Lucas'
}

caso eu queira pegar apenas os valores de um dicionario eu posso usar o 

prit(filme.values())

necessario o () pois é um comando interno.

oque ele me daria disso? apenas o "Star wars" "1977" e "George Lucas"

caso eu queira apenas os indices eu posso usar o comando keys, substituindo obviamenet o values

caso eu queira ambos posso usar o comando "items" que mostra ambos de uma maneira mais "organizada"

um exemplo igual o do "enumerate" das tuplas e litas é usando o laço for com o items,
(Utilizando o dicionario filme a cima das anotações.)
for k,v in filme.items():
    print(f'O {k} é {v}')
break

você pode utilizar uma lista para organizar os dicionarios, ex

locadora=list()
filme1= { 'Titulo' : 'Star Wars',
    'Ano':1977,
    'Diretor': 'George Lucas'
}
filme2= { 'Titulo' : 'Menino Maluquinho',
    'Ano': 1995,
    'Diretor': 'Ziraldo Alves Pinto'
}
locadora.append(filme1)
locadora.append(filme2)
print(locadora)


Uma outra forma de poder ver os itens do dicionario dentro de uma lista é usar o seguinte print.

print(locadora[0]['Titulo'])

colocamos em pratica agora:

locadora=list()
filme=dict()
for c in range(0,3):
    filme['Titulo']=str(input('Digite o titulo do filme: '))
    filme['Ano']=int(input('Digite o ano de lançamento do filme: '))
    locadora.append(filme.copy())
print(locadora)

for e in locadora:
    for k,v in e.items():
        print(f'o campo {k} tem valor {v}.')

        
Perfeito.

colocar o dicionario em ordem =

colocamos um programa de dados tipo esse :


import random
import operator
from time import sleep
resultado=list()
jogador=dict()

for c in range(1,5):
    jogador['nome']=str(input(f'Digite o nome do jogador {c}: '))
    jogador['jogada']=random.randint(1,6)
    sleep(1)
    print(f'o jogador {jogador["nome"]} tirou {jogador["jogada"]} no dado!')
    resultado.append(jogador.copy())


e para colocar em ordem basta usar o sorted ouse ja coloqeu em baixo dessa forma utilizando a importação chamada operator, para pegar o itemgetter.

ranking= sorted(jogo.items(), key=itemgetter(1), reverse=True)

o item getter serve pra pegar o 2 tipo de entrada, ou seja os numeros sorteados e não o primeiro que seria ordem alfabetica.

e basta colocar o reverse pra ficar do maior para o menor.

ele acaba virando uma lista, e ai vc deve tratar ele como uma lista.





Função!

função nada mais nada menos é do que criar um tipo de uma função estilo o print, ou o str, ou o int, só que da forma que nós queremos, ou seja, da minha necessidade

a função pode ser criada usando a palavra "def"

def MostraLinha()
    print('_'*20)

    
MostraLinha()
print('Cadastro de Aluno')
MostraLinha()


esse é um exemplo perceptivel da criação de uma função.

podemos tambem colocar parametros, digamos que tenho que fazer uma função que envia uma mensagem.

def mensagem(msg)
    print('-'*30)
    print(msg)  note que não tem aspas
    print('-'*30)

e como ficaria?

exatamente assim:

mensagem('Olá, você recebeu uma mensagem')


literalmente essa unica linha é todo o codigo.

podemos fazer tb umka função de soma. ex:

def soma(a,b):
    print(f'A = {a} e B={b})
    s=a+b
    print(f'A soma de {a} + {b} é: {s})

break

enpacotamento de dados.

quando você não souber quantos itens sera colocados dentro dos parenteses você deve usaro  * para indicar que pode ser varios EX:

def contador(*num):

e podemos fazer um programa que le a quantidade de valores


def contador(8num)
    tamanho=len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números)


agora vamos usar uma lista.

ex:

def dobrar(list)
    
Interactive help - 

pode ser chamado pela função help()

utilizado pelo console e basta colocar o comando que deseja saber oque faz. não só isso como tb serve para biblioteca, para sair basta escrever "quit"

alem do help existe o __doc__
serve da mesma forma mas pode ser usado em um print EX:
print(input.__doc__)
pronto mesma coisa que o: 
help(input)
mas com algumas modificações na fala.


Docstrings-

vc cria o manual da def que vc criou, basta colocar 3 aspas duplas e fechar logo em seguidam tudo oque foi escrito ali é a docstring

Parâmetros Opcionais:

são parametros que podem ser usados ou não, ex:

def somar(a,b,c):
    s=a+b+c
    print(f'A soma vale {s}')
nessa def caso o usuario não coloque o C daria problema, mas posso contornar isso simplesmente fazendo o seguinte ato: 
def somar(a,b,c=0):
    s=a+b+c
    print(f'A soma vale {s}')
sim, exatamento, posso apenas definir a variavel para caso ela nunca seja colocada.



Escopo de variaveis:
escopo = lugar aonde a variavel vai existir.

escopo local = aonde a variavel só vai existir em um lugar especifio, por exemplo apenas dentro de uma def

escopo global = aonde a variavel sera puxada mesmo estrando em outras def ou não


retornando valores - Return:

ele retorna o valor para algo antes da def EX:

def somar(a=0,b=0,c=0):
    s=a+b+c
    return s

resp = somar(3,2,5)

resp recebe o return.

ai a gente pode brincar exatamente assim:

r1=somar(3,2,5)
r2=somar(1,5)
r3=somar(4)
print(f'A soma dos valores deu: {r1}, {r2} e {r3}.)





"""
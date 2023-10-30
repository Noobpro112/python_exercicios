quantidade_produtos=int(input("Digite a quantidades de produtos pegos : "))
total = 0
produto_1000=0
nome_produto_caro=''
preco_produto_caro=0
while quantidade_produtos>-1:
    nome=str(input("Qual o nome do produto? ")).lower()
    preco=float(input("Qual o preço do produto? "))
    total+=preco
    quantidade_produtos-=1
    for i in range(quantidade_produtos):
        if i == 1 :
            nome_produto_caro = nome
            preco_produto_caro = preco
        elif preco>preco_produto_caro:
            nome_produto_caro = nome
            preco_produto_caro=preco
    if preco>=1000:
        produto_1000+=1
    if quantidade_produtos == 0:
        quantidade_produtos = int(input("Você quer continuar? escolha a quantidade de numero. "))
if nome == 'não':
    print(f"A quantidade de produtos acima de 1000$ foi {produto_1000} o nome do produto mais caro é {nome_produto_caro} e o preço total da compra deu {total}.")
print(f"A quantidade de produtos acima de 1000$ foi {produto_1000} o nome do produto mais caro é {nome_produto_caro} e o preço total da compra deu {total}$.")
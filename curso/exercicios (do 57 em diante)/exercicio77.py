tupla = ('casa', 'amigo', 'gato', 'pato', 'bola', 'sapato', 'cachorro', 'mesa', 'livro', 'pessoa')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in tupla:
    vogais_na_palavra = []
    for letra in palavra:
        if letra in vogais:
            vogais_na_palavra.append(letra)
    print(f"As vogais em **{palavra}** são: **{' '.join(vogais_na_palavra)}**.")

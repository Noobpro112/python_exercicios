palavra = input('Digite algo:')
print('O tipo primitivo dessa palavra é:' , type(palavra))
print('Só tem espaços?', palavra.isspace()) #o () depois do .isspace significa  (self) dele mesmo, ou seja ele vai verificar ele mesmo que seria a variavel palavra
print('é alfanumérico?', palavra.isalnum())
print('é alfabético?', palavra.isalpha())
print('está em maiúsculas', palavra.isupper())
print ('Esta capitalizada? ', palavra.istitle() )
print('é apenas numeros?' , palavra.isnumeric())

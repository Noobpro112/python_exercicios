num1 = int ( input (' Qual é o primeiro numero ? '))
num2 = int ( input (' Qual é o segundo número ? '))
num3 = int ( input (' Qual é o Terceiro número ? '))
if num1>num2:
    if num1>num3:
        print('O maior valor digitado foi {} '.format(num1))
if num2>num1:
    if num2>num3:
        print('O maior valor digitado foi {}'. format(num2) )
if num3>num1:
    if num3>num2:
     print('O maior valor digitado foi {}'.format(num3))


if num1<num2:
    if num1<num3:
        print('O menor valor digitado foi {} '.format(num1))
if num2<num1:
    if num2<num3:
        print('O menor valor digitado foi {}'. format(num2) )
if num3<num1:
    if num3<num2:
     print('O menor valor digitado foi {}'.format(num3))

import random
aluno=random.randint(1,4)
aluno1=str(input('Qual o nome do aluno 1?'))
aluno2=str(input('Qual o nome do aluno 2?'))
aluno3=str(input('Qual o nome do aluno 3?'))
aluno4=str(input('Qual o nome do aluno 4?'))
if aluno == 1:
    print('O aluno sorteado foi numero {} e deve apagar o quadro.'.format(aluno1))
if aluno == 2:
    print ('O aluno sorteado foi número {} e deve apagar o quadro'.format(aluno2))
if aluno == 3:
    print ('O aluno sorteado foi número {} e deve apagar o quadro '. format(aluno3))
if aluno == 4 :
    print ('O aluno sorteado foi número {} e deve apagar o quadro .' .format(aluno4))
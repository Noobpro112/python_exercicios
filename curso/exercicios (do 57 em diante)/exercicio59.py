while True:
    n1 = float(input("Escolha um número: "))
    n2 = float(input("Escolha outro número: "))
    
    while True:
        print("O que deseja fazer?")
        print("1 - para soma")
        print("2 - para multiplicar")
        print("3 - para o maior número")
        print("4 - para mudar os números")
        print("5 - para sair do programa")
        
        escolha = int(input("E aí, qual é a sua escolha? "))
        
        if escolha == 1:
            n3 = n1 + n2
            print("Sua soma é {}".format(n3))
        elif escolha == 2:
            n3 = n1 * n2
            print("Sua multiplicação é {}".format(n3))
        elif escolha == 3:
            if n1 > n2:
                print("O número {} é maior que o número {}".format(n1, n2))
            else:
                print("O número {} é maior que o número {}".format(n2, n1))
        elif escolha == 4:
            n1 = float(input("Qual vai ser o seu primeiro número? "))
            n2 = float(input("E o segundo? "))
        elif escolha == 5:
            break
        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")
    
    if escolha == 5:
        break
print("Acabou!")

#Precisei do chatGPT, olharei no curso como fazer e irei corrigir!

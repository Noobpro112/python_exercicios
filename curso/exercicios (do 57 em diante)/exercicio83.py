while True:
    lista=[]
    palavra=input('Digite uma palavra que possa usar parenteses: ')
    lista.extend(palavra)
    c=lista.count('(')
    c_contratrio=lista.count(')')
    if c==c_contratrio:
        print('Está fechado corretamente.')
    else:
        print('Não foi bem fechado')
        c_falta=c-c_contratrio
        print(f'Falta {c_falta} parenteses para ser fechado.')
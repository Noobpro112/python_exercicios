def voto(nasc):
    """
    ->  Calcula uma idade e mostra se o voto é:
            NEGADO, OPCIONAL ou OBRIGATÓRIO
        Se a idade for menor que 0:         ERRO
        Se a idade estiver entre 0 e 15:    NEGADO
        Se a idade estiver entre 16 e 17:   OPCIONAL
        Se a idade for maior ou igual à 60: OPCIONAL
        Se a idade estiver entre 18 e 59:   OBRIGATÓRIO
    :param nasc: Data de nascimento
    :return: Mensagem informando a idade e o voto.
    #
    """
    from datetime import date#
    i = date.today().year - nasc #
    if i <= 0:
        msg = f'ERRO: Idade menor que 0.'
    elif i < 16:
        msg = f'Com {i} anos: VOTO NEGADO.'
    elif 16 <= i < 18 or i >= 60:
        msg = f'Com {i} anos: VOTO OPCIONAL.'
    else:
        msg = f'Com {i} anos: VOTO OBRIGATÓRIO.'
    return msg


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))

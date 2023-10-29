print("Você precisa se alistar? Descubra aqui!")
idade=int(input("Quantos anos você tem? "))
mes=int(input("Em que mês estamos? (numero)  "))

if idade==18:
    print("Você deve ir se alistar esse ano! ")
    if mes==6:
        print("O ULTIMO MÊS PARA SE ALISTAR! VÁ RÁPIDO.")
    elif mes>6:
        mes_que_falta=mes-6
        print("Você já perdeu o prazo BISONHO. já passou {} mes!" .format(mes_que_falta))
    elif mes<6:
        mes_que_falta=6-mes
        print("Você ainda tem tempo para se alistar. falta {} meses para se alistar.".format(mes_que_falta))
elif idade>18:
    print("Você já deveria ter ido se alistar bizonho! ")
    if mes==6:
        print("O ULTIMO MÊS PARA SE ALISTAR! VÁ RÁPIDO.")
    elif mes>6:
        mes_que_falta=mes-6
        print("Você já perdeu o prazo BISONHO. já passou {} mes! agora só ano que vem." .format(mes_que_falta))
    elif mes<6:
        mes_que_falta=6-mes
        print("Você ainda tem tempo para se alistar. falta {} meses para se alistar.".format(mes_que_falta))

elif idade<18:
    print("Você ainda vai ter sua hora para se alistar. Fique de olho e atento as inscrições!")
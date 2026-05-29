from Fluxo import menu_veiculo , menu_turno , entregadores
def cadastrar_entregador():
    print("\n===== CADASTRAR ENTREGADOR =====")

    id_entregador = input("ID do Entregador (4 digitos): ")
   
    if len(id_entregador) != 4:
        print("ID invalido")
        return
    
    if id_entregador in entregadores:
        print("Entregador ja esta cadastrado")
        return
    
    nome = input ("Nome do Entregador:")
    
    if not nome:
        print("Nome nao pode estar vazio")
        return
   
    menu_veiculo()
    
    opcao_veiculo = input("Opcao:")

    if opcao_veiculo =="1":
        veiculo= "Moto"
    elif opcao_veiculo == "2":
        veiculo = "Carro"
    elif opcao_veiculo == "3":
        veiculo = "Van"
    else:
        print("opcao invalida")
        return
    
    menu_turno()
    
    opcao_turno = input("Opcao:")
    if opcao_turno =="1":
        turno = "Matutino"
    elif opcao_turno == "2":
        turno = "Vespertino"
    elif opcao_turno == "3":
        turno = "Noturno"
    else:
        print("opcao invalida")
        return
    
    entregadores [id_entregador] = {
        
    "id":id_entregador,
    "nome":nome,
    "veiculo": veiculo,
    "turno":turno,
    "disponivel": True,
    "pedidos":[]


    }
    print(f"Entregador {nome} cadastrado com sucesso")
    

pedidos = {}

MAPA_ESTADOS = {
    1: "AC",
    2: "AP",
    3: "SUL",
    4: "PA",
    5: "RO",
    6: "RR",
    7: "PARA"
}

MAPA_REGIOES = {
    1: "ZONA NORTE",
    2: "ZONA SUL",
    3: "ZONA LESTE",
    4: "ZONA OESTE",
    5: "CENTRO"
}

MAPA_STATUS_PEDIDO = {
    1: "PENDENTE",
    2: "EM ROTA",
    3: "ENTREGUE",
    4: "CANCELADO",
    5: "REEMBOLSADO"
}

MAPA_STATUS_PAGO = {
    1: "PAGO",
    2: "NAO PAGO",
    3: "REEMBOLSADO"
}


def id_valido(id_pedido):

    return (
        len(id_pedido) == 5 and
        id_pedido[0].isalpha() and
        id_pedido[1:].isdigit()
    )


def cadastrar_pedido():

    print("\n--- CADASTRO DE PEDIDO ---")

    erro = False

    id_pedido = input("ID do Pedido: ").upper()

    if not id_valido(id_pedido):
        print("[ERRO] Formato inválido")
        erro = True

    elif id_pedido in pedidos:
        print("[ERRO] Já existe um pedido com esse ID.")
        erro = True

    if not erro:

        nome = input("Nome do Cliente: ")

        if not nome:
            print("[ERRO] Nome não pode ser vazio.")
            erro = True

    if not erro:

        endereco = input("Endereço de Entrega: ")

        if not endereco:
            print("[ERRO] Endereço não pode ser vazio.")
            erro = True

    if not erro:

        print("Prioridade:")
        print("1 - Alta")
        print("2 - Normal")

        opcao = input("Opção: ")

        if opcao == "1":
            prioridade = "Alta"

        elif opcao == "2":
            prioridade = "Normal"

        else:
            print("[ERRO] Opção inválida.")
            erro = True

    if not erro:

        descricao = input("Descrição do Pedido: ")

        if not descricao:
            print("[ERRO] Descrição não pode ser vazia.")
            erro = True

    if not erro:

        status = "Pendente"
        id_entregador = None

        pedido = {
            "id": id_pedido,
            "cliente": nome,
            "endereco": endereco,
            "prioridade": prioridade,
            "descricao": descricao,
            "status": status,
            "id_entregador": id_entregador
        }

        pedidos[id_pedido] = pedido

        print(f"Pedido {id_pedido} cadastrado com sucesso!")
def editar_pedido():
    print("\n--- EDIÇÃO DE PEDIDO ---")

    erro = False 
    id_pedido = input("ID do pedido: ").upper()
    if not id_valido(id_pedido):
        print("[ERRO] Formato inválido")
    elif id_pedido not in pedidos:
        print("[ERRO] Pedido não encontrado")
        return
    else:
        print("\n1 - Endereço")
        print("2 - Prioridade")
        print("3 - Status")
        print("4 - Descrição")

        opcao = input("Escolha: ")
        match opcao:
            case "1":
                novo_endereco = input("Novo endereço: ")
                if novo_endereco:
                    pedidos[id_pedido]["endereco"] = novo_endereco

                    print("endereço finalizado com sucesso!")
                else:
                    print("[ERRO] Endereço inválido")
                
            case "2":
                print("\n1 - Alta")
                print("2 - Normal")
                
                prioridade = input("Escolha: ")

                if prioridade == "1":
                    pedidos[id_pedido]["prioridade"] = "Alta"
                    print("Prioridade atualizada!")

                elif prioridade == "2":
                    pedidos[id_pedido]["prioridade"] = "Normal"
                    print("Prioridade atualizada!")

                else:
                    print("[ERRO] Opção inválida")
            case "3":
                print("\n1 - Pendente")
                print("2 - Em rota")
                print("3 - Entregue")
                print("4 - Cancelado")

                status = input("Escolha o status: ")
                if status == "1":
                    pedidos[id_pedido]["status"] = "pendente"
                    print("Status atualizado!")
                
                elif status == "2":
                    pedidos[id_pedido]["status"] = "Em rota"
                    print("Status atualizado!")
                
                elif status == "3":
                    pedidos[id_pedido]["status"] = "Entregue"
                    print("Status atualizado!")

                elif status == "4":
                    pedidos[id_pedido]["status"] = "Cancelado"
                    print("Status atualizado!")

                else:
                    print("[ERRO] Opção inválida")

            case "4":
                nova_descricao = input("Nova descrição: ")
                if nova_descricao:
                    pedidos[id_pedido]["descricao"] = nova_descricao
                    print("Descrição atualizada!")
                
                else:
                    print("[ERRO] Descrição inválida.")
            case _:
                print("[ERRO] Opção inválida")
def remover_pedido():
    print("\n --- REMOÇÃO DE PEDIDO ---")
    
    id_pedido = input("Digite o ID do pedido: ").upper()
    if not id_valido(id_pedido):
        print("[ERRO] Formato de ID inválido.")
        return
    if id_pedido not in pedidos:
        print("[ERRO] pedido não encontrado.")
        return
    print("\nPedido encontrado: ")
    print(pedidos[id_pedido])

    confirmacao = input("\nTem certeza que deseja remover? (s/n)").lower()

    if confirmacao == "s":
        pedidos.pop(id_pedido)
        print("Pedido removido com sucesso")
    else:
        print("Remoção cancelada")



def atualizar_pedido():
    print(" ===== ATUALIZAÇÃO DE PEDIDO =====")
    
    id_pedido = input("ID do Pedido: ")
    if id_pedido not in pedidos:
        print("Pedido nao encontrado.")
        return
    else:
    
        pedido = pedidos[id_pedido]
        print(f"Pedido encontrado:")
        print(f"Cliente: {pedido['cliente']}")
        print(f"Status atual: {pedido['status']}")
        print(f"Entregador: {pedido['id_entregador']}")
    
        print("1 - Alterar status")
        print("2 - Cancelar pedido")
        print("3 - Associar entregador")
        print("4 - Remover entregador")
        opcao = input("Opcao: ")

        match opcao:
            case "1":
            alterar_status(id_pedido)
            case "2":
            #funcao de cancelar pedido
            case "3":
            #funcao de associar entregador
            case "4":
            #funcao de remover a associacao
            case _:
            print("Opcao invalida.")



def alterar_status(id_pedido):
    
    if pedidos[id_pedido]["status"] == "Cancelado":
        print("Pedido cancelado,alteracao nao pode ser feita.")
        return
    if pedidos[id_pedido]["status"] == "Entregue":
        print("Pedido ja foi entregue.")
        return
    
    print("1 - Pendente")
    print("2 - A caminho")
    print("3 - Entregue")
    opcao = input("Novo status: ")
    
    if opcao == "1":
        pedidos[id_pedido]["status"] = "Pendente"
    elif opcao == "2":
        pedidos[id_pedido]["status"] = "A caminho"
    elif opcao == "3":
        pedidos[id_pedido]["status"] = "Entregue"
        if pedidos[id_pedido]["id_entregador"]:
            entregadores[pedidos[id_pedido]["id_entregador"]]["disponivel"] = True
    else:
        print("Opcao invalida.")
        return
    print("Status do pedido atualizado")




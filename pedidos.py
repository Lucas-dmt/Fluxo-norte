from dados import pedidos,estado, entregadores

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
        id_entregador = ""

        pedido = {
            "id": id_pedido,
            "cliente": nome,
            "endereco": endereco,
            "prioridade": prioridade,
            "descricao": descricao,
            "status": status,
            "id_entregador": id_entregador,
            "ordem": estado["contador_pedidos"]
        }

        pedidos[id_pedido] = pedido

        print(f"Pedido {id_pedido} cadastrado com sucesso!")
def editar_pedido():
    print("\n--- EDIÇÃO DE PEDIDO ---")
 
    id_pedido = input("ID do pedido: ").upper()
    if not id_valido(id_pedido):
        print("[ERRO] Formato inválido")
    elif id_pedido not in pedidos:
        print("[ERRO] Pedido não encontrado")
        return
    else:
        print("\n=== DADOS ATUAIS DO PEDIDO ===")
        print("Cliente:", pedidos[id_pedido]["cliente"])
        print("Endereço:", pedidos[id_pedido]["endereco"])
        print("Prioridade:", pedidos[id_pedido]["prioridade"])
        print("Descrição:", pedidos[id_pedido]["descricao"])
        print("Status:", pedidos[id_pedido]["status"])

        print("\n=== EDITAR O PEDIDO ===")
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
                    pedidos[id_pedido]["status"] = "Pendente"
                    print("Status atualizado!")
                
                elif status == "2":
                    if pedidos[id_pedido]["id_entregador"] == "":
                        print("[ERRO] O pedido precisa ter um entregador associado")
                    else:
                        pedidos[id_pedido]["status"] = "Em rota"

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

def relatorio_total_pedidos():
    print("\n===== TOTAL DE PEDIDOS =====")
    print(f"Total: {len(pedidos)}")



def relatorio_pedidos_por_status():
    
    print("\n===== PEDIDOS POR STATUS =====")
    pendente = 0
    em_rota = 0
    entregue = 0
    cancelado = 0
    
    for id_pedido in pedidos:
        if pedidos[id_pedido]["status"] == "Pendente":
            pendente += 1
        elif pedidos[id_pedido]["status"] == "Em rota":
            em_rota += 1
        elif pedidos[id_pedido]["status"] == "Entregue":
            entregue += 1
        elif pedidos[id_pedido]["status"] == "Cancelado":
            cancelado += 1
    
    print(f"Pendente:  {pendente}")
    print(f"Em Rota:   {em_rota}")
    print(f"Entregue:  {entregue}")
    print(f"Cancelado: {cancelado}")

def relatorio_pedidos_alta_prioridade():
    print("\n==== PEDIDOS DE ALTA PRIORIDADE ====")

    quantidade = 0

    for id_pedido in pedidos:
        if pedidos[id_pedido]["prioridade"] == "Alta":
            quantidade += 1

            print("\nID:", id_pedido)
            print("Cliente:", pedidos[id_pedido]["cliente"])
            print("Endereço:", pedidos[id_pedido]["endereco"])
            print("Descrição:", pedidos[id_pedido]["descricao"])
            print("Status:", pedidos[id_pedido]["status"])

            if pedidos[id_pedido]["id_entregador"] != "":
                print("Entregador: ", pedidos[id_pedido]["id_entregador"])
            else:
                print("Entregador: não associado.")

    if quantidade == 0:
        print("não há pedidos de alta prioridade.")

def relatorio_entregador_mais_entregas():

    print(" \n=== ENTREGADOR COM MAIS ENTREGAS ===")

    if len(entregadores) == 0:
        print("Não há entregadores cadastrados")
        return
    
    maior = -1
    id_maior = ""

    for id_entregador in entregadores:

        quantidade = len(entregadores[id_entregador]["pedidos"])

        if quantidade > maior:
            maior = quantidade
            id_maior = id_entregador
    
    print("ID: ", id_maior)
    print("Nome: ", entregadores[id_maior]["nome"])
    print("Quantidade de entregas ", maior )


def pegar_proximo_pedido():

    melhor_id = ""

    for id_pedido in pedidos:

        p = pedidos[id_pedido]

        if p["id_entregador"] == "":

            if melhor_id == "":
                melhor_id = id_pedido

            else:
                atual = pedidos[melhor_id]

                if p["prioridade"] == "Alta" and atual["prioridade"] != "Alta":
                    melhor_id = id_pedido

                elif p["prioridade"] == atual["prioridade"]:
                    if p["ordem"] < atual["ordem"]:
                        melhor_id = id_pedido

    return melhor_id

def listar_pedidos():
    print("\n==== LISTA DE PEDIDOS ====")

    if len(pedidos) == 0:
        print("Não há pedidos cadastrados.")
        return
    
    for id_pedido in pedidos:

        print("\nID:", id_pedido)
        print("Cliente:", pedidos[id_pedido]["cliente"])
        print("Endereço:", pedidos[id_pedido]["endereco"])
        print("Prioridade:", pedidos[id_pedido]["prioridade"])
        print("Descrição:", pedidos[id_pedido]["descricao"])
        print("Status:", pedidos[id_pedido]["status"])

        if pedidos[id_pedido]["id_entregador"] != "":
            print("Entregador: ", pedidos[id_pedido]["id_entregador"])
        else:
            print("Entregador: Não associado")

def buscar_pedido():
    print("\n==== BUSCAR PEDIDO ====")

    id_pedido = input("ID do pedido: ").upper()

    if id_pedido not in pedidos:
        print("[ERRO] Pedido não encontrado.")
        return

    print("\n=== DADOS DO PEDIDO ===")
    print("ID:", id_pedido)
    print("Cliente:", pedidos[id_pedido]["cliente"])
    print("Endereço:", pedidos[id_pedido]["endereco"])
    print("Prioridade:", pedidos[id_pedido]["prioridade"])
    print("Descrição:", pedidos[id_pedido]["descricao"])
    print("Status:", pedidos[id_pedido]["status"])

    if pedidos[id_pedido]["id_entregador"] != "":
        print("Entregador:", pedidos[id_pedido]["id_entregador"])
    else:
        print("Entregador: Não associado")




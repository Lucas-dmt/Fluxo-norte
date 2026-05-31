from dados import pedidos, entregadores

def buscar_pedido_por_id():
    print("\n===== BUSCAR PEDIDO POR ID =====")
    
    id_pedido = input("Digite o ID do pedido: ")
    
    if id_pedido not in pedidos:
        print("Pedido nao encontrado.")
        return
    
    print("\n--- DADOS DO PEDIDO ---")
    print(f"ID:           {id_pedido}")
    print(f"Cliente:      {pedidos[id_pedido]['cliente']}")
    print(f"Endereço:     {pedidos[id_pedido]['endereco']}")
    print(f"Prioridade:   {pedidos[id_pedido]['prioridade']}")
    print(f"Descrição:    {pedidos[id_pedido]['descricao']}")
    print(f"Status:       {pedidos[id_pedido]['status']}")
    
    if pedidos[id_pedido]['id_entregador'] != "":
        print(f"Entregador:   {pedidos[id_pedido]['id_entregador']}")
    else:
        print("Entregador:   Nao associado")

def listar_pedidos_pendentes():
#


def listar_pedidos_entregues():
    print("\n===== PEDIDOS ENTREGUES =====")
    
    encontrou = False
    
    for id_pedido in pedidos:
        if pedidos[id_pedido]["status"] == "Entregue":
            encontrou = True
            print(f"\nID: {id_pedido}")
            print(f"  Cliente:    {pedidos[id_pedido]['cliente']}")
            print(f"  Endereço:   {pedidos[id_pedido]['endereco']}")
            if pedidos[id_pedido]['id_entregador'] != "":
                print(f"  Entregador: {pedidos[id_pedido]['id_entregador']}")
            else:
                print("  Entregador: Não informado")
    
    if not encontrou:
        print("Nenhum pedido entregue.")

def listar_entregadores_disponiveis():
   #


def listar_entregas_por_entregador():
#


def menu_das_consultas():
    opcao = "0"
    while opcao != "6":
        print("\n==== CONSULTAS ====")
        print("1 - Buscar pedido por ID")
        print("2 - Pedidos pendentes")
        print("3 - Pedidos entregues")
        print("4 - Entregadores disponiveis")
        print("5 - Entregas por entregador")
        print("6 - Voltar")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1": buscar_pedido_por_id()
            case "2": #listar_pedidos_pendentes()
            case "3": listar_pedidos_entregues()
            case "4": #listar_entregadores_disponiveis()
            case "5": #listar_entregas_por_entregador()
            case "6": pass
            case _: print("opcao invalida") 

def menu_principal():
    opcao = "0"
    while opcao != "4":
        print("\n ==== Fluxo Norte ====")
        print("1 - Pedidos")
        print("2 - Listar Entregadores")
        print("3 - Gerar relatório")
        print("4 - Sair do sistema")
        opcao = input("Escolha uma opção:")
        match opcao:
            case "1":
                menu_dos_pedidos()
            case "2":
                menu_dos_entregadores()
            case "3":
                menu_dos_relatorios()
            case "4":
                print("Saindo do sistema...")
            case _:
                print("opção inválida")
def menu_dos_pedidos():
    opcao = "0"
    while opcao != "4":
        print("\n==== PEDIDOS ====")
        print("1 - Fazer pedido")
        print("2 - Editar pedido")
        print("3 - Remover pedido")
        print("4 - Voltar para o menu principal")
        opcao = input("Escolha uma opção:")
        match opcao:
            case "1":
                print("Work in progress...")
            case "2":
                print("Work in progress")
            case "3":
                print("Work in progress")
            case "4":
                menu_principal()       
def menu_dos_entregadores():
    opcao = "0"
    while opcao != "5":
        print("\n==== ENTREGADORES ==== ")
        print("1 - Cadastrar entregador")
        print("2 - Listar entregadores")
        print("3 - Associar pedido")
        print("4 - Remover associação")
        print("5 - Voltar")
        opcao = input("Escolha uma opção:")
        match opcao:
            case "1":
                print("Work in progress...")
            case "2":
                print("Work in progress...")
            case "3":
                print("Work in progress...")
            case "4":
                print("Work in progress...")
            case "5":
                menu_principal()
def menu_dos_relatorios():
    opcao = "0"
    while opcao != "5":
        print("\n==== RELATÓRIO ====")
        print("1 - Total de pedidos")
        print("2 - Pedidos por status")
        print("3 - Pedidos de Alta prioridade")
        print("4 - Entregador com mais entregas")
        print("5 - Voltar")
        opcao = input("Escolha uma opção:")
        match opcao:
            case "1":
                print("Work in progress...")
            case "2":
                print("Work in progress...")
            case "3":
                print("Work in progress...")
            case "4":
                print("Work in progress...")
            case "5":
                menu_principal()
menu_principal()

pedidos = {}
entregadores ={}


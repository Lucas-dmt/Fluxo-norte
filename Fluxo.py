# ==== PROTÓTIPO DO PROJETO ====
def menu_principal():
    opcao = 0
    while opcao != 3:
        print("\n ==== Fluxo Norte ====")
        print("1 - Pedidos")
        print("2 - Listar Entregadores")
        print("3 - Gerar relatório")
        print("0 - Sair do sistema")
        opcao = input("Escolha uma opção:")
        match opcao:
            case 1:
                menu_dos_pedidos()
            case 2:
                menu_dos_entregadores()
            case 3:
                menu_dos_relatorios()
            case _:
                print("Saindo do sistema...")
def menu_dos_pedidos():
    pass
def menu_dos_entregadores():
    pass
def menu_dos_relatorios():
    pass

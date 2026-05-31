from entregador import cadastrar_entregador, listar_entregadores, associar_pedidos, remocao_associacao, entregadores_disponiveis
from pedidos import cadastrar_pedido, editar_pedido, remover_pedido, relatorio_pedidos_por_status, relatorio_total_pedidos, relatorio_pedidos_alta_prioridade, relatorio_entregador_mais_entregas, listar_pedidos, buscar_pedido, listar_pedidos_pendentes, listar_entregas_por_entregador
from menu_auxiliares import limpar
from dados import entregadores
def menu_principal():
    opcao = "0"
    while opcao != "4":
        print("\n ==== Fluxo Norte ====")
        print("1 - Pedidos")
        print("2 - Entregadores")
        print("3 - Gerar relatório")
        print("4 - Sair do sistema")
        opcao = input("Escolha uma opção:")
        match opcao:
            case "1":
                limpar()
                menu_dos_pedidos()
            case "2":
                limpar()
                menu_dos_entregadores()
            case "3":
                limpar()
                menu_dos_relatorios()
            case "4":
                limpar()
                print("Saindo do sistema...")
            case _:
                print("opção inválida")
def menu_dos_pedidos():
    opcao = "0"
    while opcao != "6":
        print("\n==== PEDIDOS ====")
        print("1 - Fazer pedido")
        print("2 - Buscar pedido")
        print("3 - Editar pedido")
        print("4 - Remover pedido")
        print("5 - Listar pedidos")
        print("6 - Voltar para o menu principal")
        opcao = input("Escolha uma opção:")
        match opcao:
            case "1":
                limpar()
                cadastrar_pedido()
            case "2":
                limpar()
                buscar_pedido()
            case "3":
                limpar()
                editar_pedido()
            case "4":
                limpar()
                remover_pedido()
            case "5":
                limpar()
                listar_pedidos()
            case "6":
                break       

def menu_dos_entregadores():
    opcao = "0"
    while opcao != "6":
        print("\n==== ENTREGADORES ==== ")
        print("1 - Cadastrar entregador")
        print("2 - Listar entregadores")
        print("3 - Associar pedido")
        print("4 - Remover associação")
        print("5 - Entregadores disponíveis")
        print("6 - Voltar")
        opcao = input("Escolha uma opção:")
        match opcao:
            case "1":
                limpar()
                cadastrar_entregador()
            case "2":
                limpar()
                listar_entregadores()
            case "3":
                limpar()
                associar_pedidos()
            case "4":
                limpar()
                remocao_associacao()
            case "5":
                limpar()
                entregadores_disponiveis()
            case "6":
                break
def menu_dos_relatorios():
    opcao = "0"
    while opcao != "7":
        print("\n==== RELATÓRIO ====")
        print("1 - Total de pedidos")
        print("2 - Pedidos por status")
        print("3 - Pedidos pendentes")
        print("4 - Pedidos de Alta prioridade")
        print("5 - Entregador com mais entregas")
        print("6 - Entregas por entregador")
        print("7 - Voltar")
        opcao = input("Escolha uma opção:")
        match opcao:
            case "1":
                limpar()
                relatorio_total_pedidos()
            case "2":
                limpar()
                relatorio_pedidos_por_status()
            case "3":
                limpar()
                listar_pedidos_pendentes()    
            case "4":
                limpar()
                relatorio_pedidos_alta_prioridade()
            case "5":
                limpar()
                relatorio_entregador_mais_entregas()
            case "6":
                limpar()
                listar_entregas_por_entregador()
            case "7":
                break
menu_principal()

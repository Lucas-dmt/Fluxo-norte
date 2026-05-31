from dados import  entregadores, pedidos
from menu_auxiliares import menu_turno, menu_veiculo
from pedidos import pegar_proximo_pedido
def cadastrar_entregador():
    print("\n===== CADASTRAR ENTREGADOR =====")

    id_entregador = input("ID do Entregador (4 digitos): ")
   
    if len(id_entregador) != 4:
        print("ID invalido")
        return
    
    if id_entregador in entregadores:
        print("[ERRO] Já existe um entregador com esse ID.")
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
    "disponibilidade":turno,
    "disponivel": True,
    "pedidos":[]


    }
    print(f"Entregador {nome} cadastrado com sucesso")

def listar_entregadores():

    print("\n==== LISTA DE ENTREGADORES ====")
    
    if len(entregadores) == 0:
        print("Nenhum entregador cadastrado")
        return
    else:
        for id_entregador in entregadores:
            print("\nID:", id_entregador)
            print("Nome: ", entregadores[id_entregador]["nome"])
            print("Veículo: ", entregadores[id_entregador]["veiculo"])
            print("Disponibilidade: ", entregadores[id_entregador]["disponibilidade"])

def associar_pedidos():
    print("\n==== ASSOCIAR PEDIDOS ====")

    if len(pedidos) == 0:
        print("Não há pedidos cadastrados")
        return

    if len(entregadores) == 0:
        print("Não há entregadores cadastrados")
        return

    id_pedido = pegar_proximo_pedido()

    if not id_pedido:
        print("Não há pedidos pendentes.")
        return

    if pedidos[id_pedido]["id_entregador"] != "":
        print("[ERRO] Pedido já está associado.")
        return

    print("Pedido selecionado automaticamente:", id_pedido)

    print("\n=== DADOS ATUAIS DO PEDIDO ===")
    print("Cliente:", pedidos[id_pedido]["cliente"])
    print("Endereço:", pedidos[id_pedido]["endereco"])
    print("Prioridade:", pedidos[id_pedido]["prioridade"])
    print("Descrição:", pedidos[id_pedido]["descricao"])
    print("Status:", pedidos[id_pedido]["status"])

    id_entregador = input("ID do entregador: ").upper()

    if id_entregador not in entregadores:
        print("[ERRO] Entregador não encontrado.")
        return

    if len(entregadores[id_entregador]["pedidos"]) >= 2:
        print("[ERRO] Este entregador já possui o limite de 2 pedidos.")
        return

    entregadores[id_entregador]["pedidos"].append(id_pedido)

    pedidos[id_pedido]["id_entregador"] = id_entregador
    pedidos[id_pedido]["status"] = "Em rota"

    print("Pedido associado com sucesso!")

def remocao_associacao():
    print("\n=== REMOVER ASSOCIAÇÃO ===")

    id_pedido = input("ID do pedido: ").upper()

    if id_pedido not in pedidos:
        print("[ERRO] pedido não encontrando.")
        return
    
    if pedidos[id_pedido]["id_entregador"] == "":
        print("[ERRO] Esse pedido não possui entregador associado.")
        return
    
    id_entregador = pedidos[id_pedido]["id_entregador"]

    for i in range (len(entregadores[id_entregador]["pedidos"])):
        if entregadores[id_entregador]["pedidos"][i] == id_pedido:
            entregadores[id_entregador]["pedidos"].pop(i)
            break
    pedidos[id_pedido]["id_entregador"] = ""
    pedidos[id_pedido]["status"] = "Pendente"

    print("Associação removida com sucesso.")


    
    
    

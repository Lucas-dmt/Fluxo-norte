lista_pedidos = []

def cadastrar_pedido():
    print("\n--- CADASTRO DE PEDIDO ---")

id_pedido = input("ID do Pedido: ")
        if not id_valido(id_pedido):
            print("  [ERRO] Formato inválido")
            erro = True
        elif id_pedido in pedidos:
            print("  [ERRO] Já existe um pedido com esse ID.")
            erro = True
 
        if not erro:
            nome = input("Nome do Cliente: ")
            if not nome:
                print("  [ERRO] Nome não pode ser vazio.")
                erro = True
 
        if not erro:
            endereco = input("Endereço de Entrega: ")
            if not endereco:
                print("  [ERRO] Endereço não pode ser vazio.")
                erro = True
 
        if not erro:
            print("  Prioridade:  1 - Alta   2 - Normal")
            opcao = input("  Opção: ")
            if opcao == "1":
                prioridade = "Alta"
            elif opcao == "2":
                prioridade = "Normal"
            else:
                print("  [ERRO] Opção inválida.")
                erro = True
 
        if not erro:
            descricao = input("Descrição do Pedido: ")
            if not descricao:
                print("  [ERRO] Descrição não pode ser vazia.")
                erro = True


status = "Pendente" 
id_entregador = None  

lista_pedido = {
        "id": id_pedido,
        "cliente": cliente,
        "endereco": endereco,
        "prioridade": prioridade,
        "descricao": descricao,
        "status": status,
        "id_entregador": id_entregador
}

  lista_pedidos.append(pedido)
    print(f"Pedido {id_pedido} cadastrado com sucesso!")

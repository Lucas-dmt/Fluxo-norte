pedidos = {
    "P1234":{
        "cliente": "Lucas",
        "endereco": "Rua A",
        "prioridade": "Alta",
        "descricao": "Notebook",
        "status": "Pendente",
        "id_entregador": "",
        "ordem": 1
    },
    "P2468": {
        "id": "P2468",
        "cliente": "Maria",
        "endereco": "Rua B",
        "prioridade": "Normal",
        "descricao": "Livro",
        "status": "Pendente",
        "id_entregador": "",
        "ordem": 2
    },
    "A5678": {
        "id": "A5678",
        "cliente": "Joao",
        "endereco": "Rua C",
        "prioridade": "Alta",
        "descricao": "Boneco",
        "status": "Pendente",
        "id_entregador": "",
        "ordem": 3
    }    

}

entregadores = {
    "1234": {
        "nome": "Carlos",
        "veiculo": "Van",
        "disponibilidade": "Vespertino",
        "pedidos": []
    },
    "5678": {
        "nome": "Pedro",
        "veiculo": "Moto",
        "disponibilidade": "Matutino",
        "pedidos": []
    }
}

estado = {
    "contador_pedidos":0
}

MAX_PEDIDOS = 2
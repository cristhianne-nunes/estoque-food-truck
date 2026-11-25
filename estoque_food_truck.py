# Estoque do Food Truck
produtos = ["Pão de Hot Dog", "Salsicha", "Batata Palha"]
estoque = [100, 120, 30]
minimos = [20, 30, 5]

opcao = ""

while opcao != "5": 
    print("=======================================")
    print(" GESTÃO DE ESTOQUE - HOT DOG ")
    print("=======================================")
    print("1. Visualizar Estoque e Alertas")
    print("2. Atualizar Estoque (Entrada de Produtos)")
    print("3. Registrar Venda (Dar Baixa automática)")
    print("4. Pesquisar Produto no Estoque")
    print("5. Sair do Programa")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == "1":
        #ORDENAÇÃO: Coloca o estoque do menor para o maior
        volta = 0
        while volta < 3:
            posicao = 0
            while posicao < 2:
                if estoque[posicao] > estoque[posicao + 1]:
                    estoque[posicao], estoque[posicao + 1] = estoque[posicao + 1], estoque[posicao]
                    produtos[posicao], produtos[posicao + 1] = produtos[posicao + 1], produtos[posicao]
                    minimos[posicao], minimos[posicao + 1] = minimos[posicao + 1], minimos[posicao]
                posicao = posicao + 1
            volta = volta + 1

        print("=== ESTOQUE ATUAL (ORDENADO) ===")
        posicao = 0
        while posicao < 3:
            if estoque[posicao] <= minimos[posicao]:
                print(produtos[posicao] + ": " + str(estoque[posicao]) + " unidades -> BAIXO ESTOQUE.")
            else:
                print(produtos[posicao] + ": " + str(estoque[posicao]) + " unidades -> OK")
            posicao = posicao + 1

    elif opcao == "2":
        print("Qual produto deseja abastecer?")
        print("1. Pão de Hot Dog")
        print("2. Salsicha")
        print("3. Batata Palha")
        item = input("Escolha o produto (1-3): ")

        nome_escolhido = ""
        if item == "1":
            nome_escolhido = "Pão de Hot Dog"
        elif item == "2":
            nome_escolhido = "Salsicha"
        elif item == "3":
            nome_escolhido = "Batata Palha"

        if nome_escolhido != "":
            #Procurar onde o produto está na lista
            posicao = 0
            while posicao < 3:
                if produtos[posicao] == nome_escolhido:
                    quantidade = int(input("Qual a quantidade que entrou no estoque? "))
                    estoque[posicao] = estoque[posicao] + quantidade
                    print("Estoque atualizado.")
                posicao = posicao + 1
        else:
            print("Opção de produto inválida.")

    elif opcao == "3":
        print("--- REGISTRAR VENDA ---")
        print("1. Hot Dog Simples (Consome: 1 Pão, 1 Salsicha)")
        print("2. Hot Dog Especial (Consome: 1 Pão, 1 Salsicha, 1 Batata Palha)")
        lanche = input("Escolha o lanche vendido: ")

        # Agora vamos descobrir em qual posição cada ingrediente está
        posicao = 0
        posicao_pao = 0
        posicao_salsicha = 0
        posicao_batata_palha = 0
        while posicao < 3:
            if produtos[posicao] == "Pão de Hot Dog":
                posicao_pao = posicao
            elif produtos[posicao] == "Salsicha":
                posicao_salsicha = posicao
            elif produtos[posicao] == "Batata Palha":
                posicao_batata_palha = posicao
            posicao = posicao + 1
        
        if lanche == "1":
            if estoque[posicao_pao] >= 1 and estoque[posicao_salsicha] >= 1:
                estoque[posicao_pao] = estoque[posicao_pao] - 1
                estoque[posicao_salsicha] = estoque[posicao_salsicha] - 1
                print("Venda realizada! 1 Pão e 1 Salsicha retirados do estoque.")
            else:
                print("Insumos insuficientes!")
        elif lanche == "2":
            if estoque[posicao_pao] >= 1 and estoque[posicao_salsicha] >= 1 and estoque[posicao_batata_palha] >= 1:
                estoque[posicao_pao] = estoque[posicao_pao] - 1
                estoque[posicao_salsicha] = estoque[posicao_salsicha] - 1
                estoque[posicao_batata_palha] = estoque[posicao_batata_palha] - 1
                print("Venda realizada! Estoque atualizado.")
            else:
                print("Insumos insuficientes!")
        else:
            print("Opção de lanche inválida.")

    elif opcao == "4":
        #PESQUISA SEQUENCIAL
        print("=== PESQUISAR PRODUTO ===")
        busca = input("Digite o nome exato do produto (Pão de Hot Dog, Salsicha ou Batata Palha): ")

        posicao = 0
        achou = "não"

        while posicao < 3:
            if produtos[posicao] == busca:
                print("Produto encontrado: " + produtos[posicao] + " Quantidade: " + str(estoque[posicao]))
                achou = "sim"
            posicao = posicao + 1

        if achou == "não":
            print("Produto não encontrado no estoque.")

    elif opcao == "5":
        print("Encerrando o sistema do Food Truck.")
        
    else:
        print("Opção inválida! Digite um número de 1 a 5.")

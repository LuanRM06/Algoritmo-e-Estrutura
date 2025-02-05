def menu():
    fila_impressao = FilaDeimpressao()
    fila_impressao.configurar_inicial()
    while True:
        print("Opções:")
        print("1 = Adicionar um trabalho na fila de impressão")
        print("2 = Imprimir o próximo trabalho da fila")
        print("3 = Mostrar a fila de impressão")
        print("4 = Sair")
        escolha = input("Escolha uma opção 1-4")
        
    if escolha == "1":
        trabalho = input("Digite o nome do trabalho a ser impresso")
        fila_impressao.adicionar_trabalho(trabalho)
        
    elif escolha == "2":
        fila_impressao.processar_trabalho()
        
    elif escolha == "3":
        fila_impressao.mostrar_fila()
        
    elif escolha == "4":
        print("Saindo do programa...")
        
    else:
        print("Opção Inválida.")
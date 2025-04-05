def lista_compras():
    while True:
        print("1. Exibir Lista de compras")
        print("2. Adicionar item à lista")
        print("3. Retirar item à lista")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")
        lista_completa = []

        if escolha == 'S' or escolha == 's' or escolha == '4':
            print("Até a próxima!")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opão invalida, tente novamente!")
            continue

        if escolha == '1':
            print(lista_completa)





lista_compras()
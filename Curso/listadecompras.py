from decorator import append


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
            for item in lista_completa:
                print(item)

        if escolha == '2':
            lista_completa.append(input("Adicone um item: "))
            for cada in lista_completa:
                print(cada)
                continue



lista_compras()
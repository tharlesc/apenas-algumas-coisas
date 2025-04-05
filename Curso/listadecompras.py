def lista_compras():

    lista_completa = []

    while True:
        print("1. Exibir Lista de compras")
        print("2. Adicionar item à lista")
        print("3. Retirar item à lista")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == 'S' or escolha == 's' or escolha == '4':
            print("Até a próxima!")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opão invalida, tente novamente!")
            continue

        if escolha == '1': #ver lista
            if not lista_completa:
                print("Sua lista está vazia!")
            else:
                for indice, item in enumerate(lista_completa):
                    print(indice, "-", item)

        if escolha == '2': #Adicionar item

            lista_completa.append(input("Adicone um item: "))
            for cada in lista_completa:
                print('Item adicionado: ', cada)
                # if len(lista_completa) > '0':
                #     print('Contém ', len(lista_completa), 'itens em sua lista')
                # else:
                #     print('Ops! Ainda não adicionou nenhum item!')

        if escolha == '3': #retirar item
            if not lista_completa:
                print("Ops! Sua lista ainda está vazia!")
            else:
                for atual, coisas in enumerate(lista_completa):
                    print(atual, '-', coisas)

                    retirada = int(input("Digite o item que você deseja retirar: "))
                    retirado = lista_completa.pop(retirada)
                    print(f"O item '{retirado}' foi descartado!")





lista_compras()
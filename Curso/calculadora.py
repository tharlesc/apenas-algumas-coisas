def calculadora():
    while True:
        print("Calculadora Simples")
        print()
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        operacao = input("Selecione uma opção ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("Obrigado por usar a calculadora")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("opção invalida tente novamente")
            continue

        numero1 = float(input("DIGITE UM NÚMERO: "))
        numero2 = float(input("DIGITE UM NÚMERO: "))

        if operacao == '1':

            resultado = numero1 + numero2

            print("O resultado da soma é:", resultado)
        elif operacao == '2':
            resultado = numero1 - numero2
            print("O resultado da subtração é:", resultado)
        elif operacao == '3':
            resultado = numero1 * numero2
            print("O resultado da multiplicação é:", resultado)
        elif operacao == '4':
            resultado = numero1 / numero2
            print("O resultado da divisão é:", resultado)
        else:
            if numero2 == 0:
                print("Divisão por 0 não são possível")
                continue
            else:
                resultado = numero1 / numero2
                print("O resultado da soma é:", resultado)

calculadora()
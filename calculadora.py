while True:
    print("\nCalculadora usando while")
    print("Escolha a operação:")
    print("1 Soma")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão")
    print("5 Sair")

    digito = input("Digite o número da operação desejada: ")

    if digito == "5":
        print("Calculadora desligada")
        break

    if digito not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        continue

    if digito == "1":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif digito == "2":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif digito == "3":
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif digito == "4":
        print(f"Resultado: {num1} / {num2} = {resultado}")

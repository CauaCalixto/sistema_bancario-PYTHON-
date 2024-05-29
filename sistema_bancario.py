menu = """
[1] Depositar
[2] Sacar
[3] Extrato Bancário
[4] Sair """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
Limite_Saque = 3
saques_realizado = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Olá, Seja Bem-Vindo ao nosso Banco! \nDigite o valor que será depositado: "))
        if deposito >= 0:
            print("O valor de depósito e inválido. Tente Novamente!")
        else:
            saldo += deposito
            extrato += print(f"Depósito: R$ {deposito:.2f}\n")
            print('Depósito feito com sucesso!')

    elif opcao == "2":
        if saques_realizado < Limite_Saque:
            valor_saque = float(input("Digite o valor que será sacado: R$"))
            if valor_saque > limite:
                print("Valor de saque excede o limite máximo permitido de R$ 500.00")
            elif valor_saque > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= valor_saque
                saques_realizado += 1
                extrato += print(f"Saque: R$ {valor_saque:.2f}")
                print("Saque realizado com sucesso!")
        else:
            print("Número máximo de saques diários atingido.")
    elif opcao == "3":
        print("\n--- Extrato Bancário ---")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print('-----------------------------\n')
    elif opcao == "0":
        print("Foi um prazer, Volte Sempre!")
        break
    else:
        print("Opção inválida. Tente novamente!")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

Saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            Saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Operação Falhou! O valor informado é invalido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > Saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação Falhou! Número máximo de saques excedido.")

        elif valor > 0:
            Saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Operação Falhou! O valor informado é invalido.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {Saldo: .2f}")
        print("================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")






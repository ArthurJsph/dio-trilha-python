menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Deposito")
        valor = float(input("Coloque o valor do depósito: "))
        if valor > 0:
            saldo += valor
            deposito = f"Deposito R$: {valor}"
            extrato += deposito + "\n"

    elif opcao == "2":
        print("Sacar")
        valor = float(input("Coloque o valor do saque: "))

        ultrapassou_saldo = valor > saldo
        ultrapassou_limite = valor > limite
        ultrapassou_saques = numero_saques >= LIMITE_SAQUES

        if ultrapassou_saldo:
            print("Operação não concluída! Saldo insuficiente.")
        elif ultrapassou_limite:
            print("Operação não concluída! O valor do saque ultrapassa o limite.")
        elif ultrapassou_saques:
            print("Operação não concluída! O número máximo de saques foi atingido.")
        elif valor > 0:
            saldo -= valor
            saque = f"Saque: R$ {valor}"
            extrato += saque + "\n"
            numero_saques += 1

    elif opcao == "3":
        print("Extrato")
        print(extrato if extrato else "Não houve nenhuma movimentação realizada")
        print(f"Saldo: R$ {saldo}")

    elif opcao == "4":
        break

    else:
        print("Operação não concluída, por favor selecione novamente a opção desejada: ")
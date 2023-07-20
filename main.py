menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""
saldo = 0
limite = 5000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    match opcao:
        case "d":
            valor = float(input("Informe o valor do deposito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Deposito: R$ {valor:.2f}"
            else:
                print("Operacao falhou! Valor informado invalido.")
        case "s": 
            valor = float(input("Informe o valor do saque: "))
            if valor > saldo:
                print("Saldo insuficiente!")
            elif valor > limite:
                print("O valor do saque excede o limite!")
            elif numero_saques >= LIMITE_SAQUES:
                print("Numero de saques excedidos!")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}"
                numero_saques +=1
            else:
                print("Valor informado invalido.")
        case "e":
            print("\n=====Extrato=====")
            print("Nao foram realizados movimentacoes" if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("\n================")
        case "q":
            break
        case _:
            print("Opcao invalida.")

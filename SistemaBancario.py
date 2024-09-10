menu = """
SEJA BEM-VINDO! SELECIONE A OPÇÃO DESEJADA:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Valor a ser depositado: "))

        if valor > 0:
          saldo += valor
          extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
         print("Valor informado inválido, tente novamente!")
        
    elif  opcao == "s":
          valor = float(input("informe o valor do saque: "))

          excedeu_saldo = valor > saldo
          excedeu_limite = valor > limite
          excedeu_saques = numero_saques >= LIMITE_SAQUES

          if excedeu_saldo:
           print("Saldo insuficiente!")
          elif excedeu_limite: print("O valor do saque excedeu o limite.")
          elif excedeu_saques:
           print("Número máximo de saques atingido.")
            
          elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
          else:
            print("Valor informado inválido. Operação cancelada.")

    elif opcao == "e":
     print("\n================EXTRATO===============")
     print("Não foram realizadas movimentações" if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("======================================")
    elif opcao == "q": 
     break

else:
    print("Operação inválida, selecione novamente a operação desejada.")
    
#Desafio DIO - Criar um sistema bancário com Python
deposito=0
opcao=-1
saldo=0
numero_saque=0
LIMITE_DIARIO=3
limite_saque=500
saque=0
extrato=""
menu='''
[1] Pressione 1 para saldo
[2] Pressione 2 para saque
[3] Pressione 3 para deposito
[4] Pressione 4 para extrato
[0] Pressione 0 para sair'''

while opcao != 0:
    print("#"*59,menu)
    print("#"*59)
    opcao=int(input(""))
    
    if opcao == 1:
        print(f"Seu saldo é R${saldo:.2f}\n\n")
    
    elif opcao == 2:
        saque=float(input("Digite o valor do saque R$"))
        if saque<=0:
            print("Operação falhou! Digite um valor válido.")
        if saque<=saldo and numero_saque<3 and saque>0 and saque<=limite_saque:
            saldo-=saque
            numero_saque+=1
            extrato+=(f"Saque de R${saque:.2f} realizado.\n")
        if saque>saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif numero_saque==LIMITE_DIARIO:
            print("Operação falhou! Você realizou o limite de saques diários.")
        elif saque>limite_saque:
            print("Operação falhou! Limite de saque excedido.")
                
    
    if opcao == 3:
        deposito=float(input("Digite o valor do depósito R$"))
        if deposito > 0:
            saldo+=deposito
            extrato+= (f"Depósito de R$ {deposito:.2f} realizado.\n")
            if deposito<0:
                print("Operação falhou! Digite um valor válido.")
    
    if opcao == 4:
        print("######################### Extrato #########################\n\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu saldo é de R${saldo:.2f}.\n\n")
        print("###########################################################")
   
    elif opcao == 0:
        break
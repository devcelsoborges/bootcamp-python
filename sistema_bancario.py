#Desafio DIO - Criar um sistema bancário com Python
import textwrap

def menu():
    menu_text = '''
[1]\tPressione 1 para cadastrar novo usuário
[2]\tPressione 2 para criar nova conta
[3]\tPressione 3 para saldo
[4]\tPressione 4 para listar contas
[5]\tPressione 5 para saque
[6]\tPressione 6 para depósito
[7]\tPressione 7 para extrato
[0]\tPressione 0 para sair
'''
    return input(textwrap.dedent(menu_text))

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nEste CPF já está cadastrado em um usuário.")
        return
    nome = input("Digite o seu nome completo: ")
    idade = input("Digite a sua data de nascimento (dia/mês/ano): ")
    endereco = input("Digite o seu endereço (Cidade, sigla/estado, bairro, logradouro, número): ")
    usuarios.append({"nome": nome, "idade": idade, "cpf": cpf, "endereco": endereco})
    print("#################### Usuário criado com sucesso! ####################")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n#################### Usuário não encontrado, processo encerrado. ####################")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        """
        print("#" * 100)
        print(textwrap.dedent(linha))

def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("Operação falhou! Digite um valor válido.")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    print("Depósito realizado com sucesso!")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print("Operação falhou! Limite de saque excedido.")
    elif excedeu_saques:
        print("Operação falhou! Você realizou o limite de saques diários.")
    elif valor <= 0:
        print("Operação falhou! Digite um valor válido.")
    else:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Operação de saque realizada com sucesso!")
    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("######################### Extrato #########################\n\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSeu saldo é de R${saldo:.2f}.\n\n")
    print("###########################################################")

def main():
    usuarios = []
    contas = []
    LIMITE_DIARIO = 3
    AGENCIA = "0001"
    opcao = -1
    saldo = 0
    numero_saque = 0
    limite_saque = 500
    extrato = ""
    
    while opcao != 0:
        opcao = int(menu())
        print("#" * 59)
        
        if opcao == 1:
            criar_usuario(usuarios)
        elif opcao == 2:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 3:
            print(f"Seu saldo é R${saldo:.2f}\n\n")
        elif opcao == 4:
            listar_contas(contas)
        elif opcao == 5:
            saque = float(input("Digite o valor do saque R$"))
            saldo, extrato = sacar(saldo, saque, extrato, saldo, numero_saque, LIMITE_DIARIO)
        elif opcao == 6:
            deposito = float(input("Digite o valor do depósito R$"))
            saldo, extrato = depositar(saldo, deposito, extrato)
        elif opcao == 7:
            exibir_extrato(saldo, extrato)
        elif opcao == 0:
            break

main()
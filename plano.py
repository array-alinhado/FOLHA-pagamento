import os
os.system("cls || clear")

def limpar_tela():
    os.system("cls || clear")

def calcular_inss(salario_bruto):
    # Lógica do cálculo do INSS
    if salario_bruto < 1100.00:
        return salario_bruto * 0.075
    elif salario_bruto <= 2203.48:
        return salario_bruto * 0.09
    elif salario_bruto <= 3305.22:
        return salario_bruto * 0.12
    elif salario_bruto <= 6433.57:
        return min(salario_bruto * 0.14, 854.36)
    else:
        return 854.36

def calcular_irrf(salario_bruto, dependentes):
    # Lógica do cálculo do IRRF
    deducacao_dependentes = dependentes * 189.59
    salario_liquido = salario_bruto - calcular_inss(salario_bruto) - deducacao_dependentes

    if salario_liquido < 2259.20:
        return 0
    elif salario_liquido <= 2826.65:
        return salario_liquido * 0.075
    elif salario_liquido <= 3751.05:
        return salario_liquido * 0.15
    elif salario_liquido > 4664.68:
        return salario_liquido * 0.225
    else:
        return salario_liquido * 0.275

def calcular_vale(salario_bruto, vale_transport):
    if vale_transport:
        return salario_bruto * 0.006
    return 0

def calcular_vale_refeicao(vale_refeicao):
    return vale_refeicao * 0.020

def calcular_plano(dependentes):
    return dependentes * 150

def adicionar_empregado():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    idade = int(input("Digite sua idade: "))
    matricula = input("Digite a matrícula do funcionário: ")
     
     # Definindo a senha com confirmação
    while True:
        senha = input("Digite a senha do funcionário: ")
        senha_confirmada = input("Confirme a senha: ")
        if senha == senha_confirmada:
            break
        else:
            print("As senhas não coincidem. Tente novamente.")

    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade,
        "matricula": matricula,
        "senha": senha
    }

def calcular_folha(empregado):
    salario_bruto = float(input(f"Digite o salário bruto de {empregado['nome']} {empregado['sobrenome']}: "))
    vale_transport = input("Quer ter o vale transporte? [S/N]: ").upper().strip() == 'S'
    vale_refeicao = float(input("Digite o valor do vale fornecido pela empresa: "))
    
    dependentes = int(input("Quantos dependentes você possui? "))

    desconto_inss = calcular_inss(salario_bruto)
    desconto_irrf = calcular_irrf(salario_bruto, dependentes)
    desconto_vale_transport = calcular_vale(salario_bruto, vale_transport)
    desconto_vale_refeicao = calcular_vale_refeicao(vale_refeicao)
    desconto_plano_saude = calcular_plano(dependentes)

    total_descontos = (desconto_inss + desconto_irrf + desconto_vale_transport + desconto_vale_refeicao + desconto_plano_saude)
    salario_liquido = salario_bruto - total_descontos

    # Exibe os resultados
    print(f"\n--- Folha de Pagamento de {empregado['nome']} {empregado['sobrenome']} ---")
    print(f"Salário Base: R$ {salario_bruto:.2f}")
    print(f"Desconto INSS: R$ {desconto_inss:.2f}")
    print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {desconto_vale_transport:.2f}")
    print(f"Desconto Vale Refeição: R$ {desconto_vale_refeicao:.2f}")
    print(f"Desconto Plano de Saúde: R$ {desconto_plano_saude:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}\n")
    

def menu():
    empregado = {}
    while True:
        print("=== Sistema de Folha de Pagamento ===")
        print("1. Adicionar empregado")
        print("2. Calcular Folha de Pagamento")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            empregado = adicionar_empregado()
            limpar_tela()
        elif opcao == "2":
           if empregado:
                senha_digitada = input("Digite a senha para calcular a folha de pagamento: ")
                if senha_digitada == empregado['senha']:  # Verifica se a senha está correta
                    calcular_folha(empregado)
                else:
                    print("Senha ta errada meu mano,tente mais tarde.")
                    break  # Encerra o programa se a senha estiver errada.
        elif opcao == "3":
            limpar_tela()
            print("Saindo do sistema...")
            print("FAZ O LLLLLL")
            break
        else:
            limpar_tela()
            print("Opção inválida! Tente novamente.")

# Iniciar o sistema com o menu
menu()

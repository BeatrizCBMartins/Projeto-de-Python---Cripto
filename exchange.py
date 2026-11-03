import datetime, os
extrato = "extrato.txt"
cpf = "12345678910"
senha = "123456"



def login():
    while True:
        cpf_login = input("Digite o seu CPF: ")
        if cpf_login.isdigit() and len(cpf_login) == 11:
            if cpf_login == cpf:
                while True:
                    senha_login = input("Digite sua senha: ")
                    if senha_login.isdigit() and len(senha_login) == 6:
                        if senha_login == senha:
                            print("Login aceito! \nRedirecionando para o menu... \n")
                            while True:
                                exibeMenu()
                                menu = int(input())
                                if (not processaMenu(menu)):
                                    break
                            return False
                            
                        else:
                            print("Senha incorreta!")
                    
                    else:
                        print("Por favor, insira a senha com 6 dígitos e somente com números!")           
                
            else:
                print("CPF incorreto!")
        else:
            print("Por favor, insira o CPF com 11 dígitos e somente com números!")
        
            
def exibeMenu():
    print("\n------------------------------------------------")
    print("\nBem vindo ao menu! \nDigite a opção desejada! \n")
    print("1 - Consultar saldo")
    print("2 - Consultar extrato")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Comprar criptomoedas")
    print("6 - Vender criptomoedas")
    print("7 - Atualizar cotação")
    print("8 - Sair")
    print("\n------------------------------------------------")

def processaMenu(menu):
    if menu == 1:
        senha_def()
        consultarSaldo()
        return True

    elif menu == 2:
        consultarExtrato()
        return True

    elif menu == 3:
        depositar()
        return True

    elif menu == 4:
        sacar()
        return True

    elif menu == 5:
        comprarCripto()
        return True

    elif menu == 6:
        venderCripto()
        return True

    elif menu == 7:
        attCotacao()
        return True

    elif menu == 8:
        print("Obrigado e até mais!")
        return False

    return False

def senha_def():
    while True:
        senha_login = input("Digite sua senha: ")
        if senha_login.isdigit() and len(senha_login) == 6:
            if senha_login == senha:
                print("Senha aceita! \nCarregando saldo...")
                return False

            else:
                print("Senha incorreta!")
                            
        else:
            print("Por favor, insira a senha com 6 dígitos e somente com números!")

def consultarSaldo():
    print("\n------------------------------------------------")
    print("Nome: Beatriz Martins")
    print("CPF: 123.456.789-10 \n")
    print(f"Reais: {reais}")
    print(f"Bitcoin: {bitcoin}")
    print(f"Ethereum: {ethereum}")
    print(f"Ripple: {ripple}")
    print("\n------------------------------------------------")

def depositar():
    global reais
    print("\n------------------------------------------------")
    print(f"Saldo atual (Reais): R$ {reais}")
    deposito = float(input("Digite o valor do depósito em R$: "))
    reais += deposito
    print(f"Saldo atual após o depósito (Reais): R$ {reais}")

    salvar(
        tipo = "+",
        valor = deposito,
        moeda = "REAL",
        cotacao = 0.00,
        taxa = 0.00,
        reais = reais,
        bitcoin = bitcoin,
        ethereum = ethereum,
        ripple = ripple
    )

    dep = input("Deseja fazer mais um depósito? ")
    dep = dep.lower()
    if dep == "sim":
        return depositar()
    elif dep == "não" or dep == "nao":
        return False
    else:
        print("Palavra inválida!")
        return False

def sacar():
    global reais
    print("\n------------------------------------------------")
    print(f"Saldo atual (Reais): R$ {reais}")
    saque = float(input("Digite o valor do saque em R$: "))
    if saque <= reais:
        reais -= saque
        print(f"Saldo atual após o saque (Reais): R$ {reais}")

    else:
        print("O valor do saque ultrapassa o do saldo!")
        return

    salvar(
            tipo = "-",
            valor = saque,
            moeda = "REAL",
            cotacao = 0.00,
            taxa = 0.00,
            reais = reais,
            bitcoin = bitcoin,
            ethereum = ethereum,
            ripple = ripple
        )

    sac = input("Deseja fazer mais um saque? ")
    sac = sac.lower()
    if sac == "sim":
        return sacar()
    elif sac == "não" or sac == "nao":
        return False
    else:
        print("Palavra inválida!")
        return False

def salvar(tipo, valor, moeda, cotacao, taxa, reais, bitcoin, ethereum, ripple):
    data = datetime.now().strftime("%d-%m-%Y %H:%M")

    with open(extrato, "a") as arquivo:
        arquivo.write(f"{data} {tipo}{valor:.2f} {moeda} CT: {cotacao:.2f}     TX: {taxa:.2f} REAL: {reais:.2f} BTC: {bitcoin:.2f} ETH: {ethereum:.2f} XRP: {ripple:.2f} \n")
    
def carregar():
    global reais
    if not os.path.exists(extrato):
        return
    with open(extrato, "r") as arquivo:
        for linha in arquivo:
            tipo, valor, moeda, cotacao, taxa, reais, bitcoin, ethereum, ripple = linha.strip()
            reais = reais
        print(reais)
    
    
  





carregar()
login()




import datetime, os, random
extrato = "extrato.txt"
cotacoes = "cotacoes.txt"
cpf = "12345678910"
senha = "123456"
reais = 0
bitcoin = 0
ethereum = 0
ripple = 0




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
                print("Senha aceita! \nCarregando... \n")
                return False

            else:
                print("Senha incorreta!")
                            
        else:
            print("Por favor, insira a senha com 6 dígitos e somente com números!")

def consultarSaldo():
    print("\n------------------------------------------------")
    print("Nome: Beatriz Martins")
    print("CPF: 123.456.789-10 \n")
    print(f"Reais: {armazenar_reais()}")
    print(f"Bitcoin: {bitcoin}")
    print(f"Ethereum: {ethereum}")
    print(f"Ripple: {ripple}")
    print("\n------------------------------------------------")

def depositar():
    global reais
    print("\n------------------------------------------------")
    print(f"Saldo atual (Reais): R$ {armazenar_reais()}")
    deposito = float(input("Digite o valor do depósito em R$: "))
    reais += deposito
    salvar(
            tipo = "+",
            valor = deposito,
            moeda = "REAL",
            cotacao = 0.00,
            taxa = 0.00,
            bitcoin = bitcoin,
            ethereum = ethereum,
            ripple = ripple
        )
    print(f"Saldo atual após o depósito (Reais): R$ {armazenar_reais()}")

    

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
    print(f"Saldo atual (Reais): R$ {armazenar_reais()}")
    saque = float(input("Digite o valor do saque em R$: "))
    if saque <= armazenar_reais():
        reais -= saque
        salvar(
                    tipo = "-",
                    valor = saque,
                    moeda = "REAL",
                    cotacao = 0.00,
                    taxa = 0.00,
                    bitcoin = bitcoin,
                    ethereum = ethereum,
                    ripple = ripple
        )
        print(f"Saldo atual após o saque (Reais): R$ {armazenar_reais()}")

    else:
        print("O valor do saque ultrapassa o do saldo!")
        return

    

    sac = input("Deseja fazer mais um saque? ")
    sac = sac.lower()
    if sac == "sim":
        return sacar()
    elif sac == "não" or sac == "nao":
        return False
    else:
        print("Palavra inválida!")
        return False

def salvar(tipo, valor, moeda, cotacao, taxa, bitcoin, ethereum, ripple):
    data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    if not os.path.exists(extrato):
            return
    with open(extrato, "a") as arquivo:
        arquivo.write(f"{data} {tipo}{valor:.2f} {moeda} CT: {cotacao:.2f}     TX: {taxa:.2f} REAL: {armazenar_reais():.2f} BTC: {bitcoin:.2f} ETH: {ethereum:.2f} XRP: {ripple:.2f} \n")

def armazenar_reais ():
    saldo_reais = 0

    if not os.path.exists(extrato):
                return
    with open(extrato, "r") as arquivo:
            for linha in arquivo:
                if not linha.strip():
                    continue
                linha_d = linha.split()
                valor = linha_d[2]
                moeda = linha_d[3]

                if moeda == "REAL":
                    if valor.find("+") == 0:
                        saldo_reais += float(valor.replace("+", ""))

                    elif valor.find("-") == 0:
                        saldo_reais += float(valor)
                    
    return saldo_reais

def consultarExtrato():
    print("Nome: Beatriz Cristina Braz Martins \nCPF: 123.456.789-10 \n")
    with open(extrato, "r") as arquivo:
        for linha in arquivo.readlines():
            print(linha)


def aleatorio(valor):
    percentual = random.uniform(-0.05, 0.05)
    valor_novo = valor * (1 + percentual)
    return valor_novo

def salvarCot (bit, eth, rip):
        with open(cotacoes, "w") as arquivo:
            arquivo.write(f"{bit}\n")
            arquivo.write(f"{eth}\n")
            arquivo.write(f"{rip}")

def carregarCot():
    if not os.path.exists(cotacoes):
        return 418588.33, 12314.08, 6.69
    
    with open (cotacoes, "r") as arquivo:
        linhas = arquivo.readlines()
        bit = float(linhas[0].strip())
        eth = float(linhas[1].strip())
        rip = float(linhas[2].strip())
        return bit, eth, rip

precoBit, precoEt, precoRip = carregarCot()
         
def attCotacao():
    global precoBit, precoEt, precoRip

    precoBit = aleatorio(precoBit)
    precoEt = aleatorio(precoEt)
    precoRip = aleatorio(precoRip)

    salvarCot(precoBit, precoEt, precoRip)

    print("Cotação atual: ")
    print(f"Bitcoin: {precoBit:.2f}")
    print(f"Ethereum: {precoEt:.2f}")
    print(f"Ripple: {precoRip:.2f}")


def comprarCripto():
    global precoBit, precoEt, precoRip

    senha_def()

    print(precoBit)





login()




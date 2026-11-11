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
                            print("\nSenha incorreta!")
                    
                    else:
                        print("Por favor, insira a senha com 6 dígitos e somente com números!")           
                
            else:
                print("\nCPF incorreto!")
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

    else:
        print("Valor inválido!")
        return True


def senha_def():
    while True:
        senha_login = input("Digite sua senha: ")

        if senha_login.isdigit() and len(senha_login) == 6:
            if senha_login == senha:
                print("\nSenha aceita! \nCarregando... \n")
                return False

            else:
                print("\nSenha incorreta!")
                            
        else:
            print("Por favor, insira a senha com 6 dígitos e somente com números!")

def consultarSaldo():
    print("\n------------------------------------------------")
    print("Nome: Beatriz Cristina Braz Martins")
    print("CPF: 123.456.789-10 \n")
    print(f"Reais: {armazenar_reais():.2f}")
    print(f"Bitcoin: {armazenar_bit():.6f}")
    print(f"Ethereum: {armazenar_eth():.6f}")
    print(f"Ripple: {armazenar_xrp():.6f}")
    print("\n------------------------------------------------")

def depositar():
    global reais

    print("\n------------------------------------------------\n")

    print(f"Saldo atual (Reais): R$ {armazenar_reais()}\n")
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
    print(f"\nSaldo atual após o depósito (Reais): R$ {armazenar_reais()}")
    print("-" * 50)

    return

def sacar():
    global reais

    print("\n------------------------------------------------\n")

    print(f"Saldo atual (Reais): R$ {armazenar_reais()}\n")
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
        print(f"\nSaldo atual após o saque (Reais): R$ {armazenar_reais()}")
        print("-" * 50)

    else:
        print("O valor do saque ultrapassa o do saldo!")
        return

    return

def salvar(tipo, valor, moeda, cotacao, taxa, bitcoin, ethereum, ripple):
    valor = round(valor, 2)
    data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    saldo_anterior = armazenar_reais()
    saldo_bit = armazenar_bit()
    saldo_eth = armazenar_eth()
    saldo_xrp = armazenar_xrp()

    if tipo == "+":
        if moeda != "REAL":
            valor_taxa = (valor * float(taxa))
            saldo_att = saldo_anterior - (valor + valor_taxa)

            if moeda == "BTC":
                saldo_bit += (valor / cotacao)

            elif moeda == "ETH":
                saldo_eth += (valor / cotacao)

            elif moeda == "XRP":
                saldo_xrp += (valor / cotacao)


        else:
            saldo_att = saldo_anterior + valor

    elif tipo == "-":
        if moeda != "REAL":
            valor_taxa = valor * float(taxa)
            saldo_att = saldo_anterior + (valor - valor_taxa)

            if moeda == "BTC":
                saldo_bit -= (valor / cotacao)
            elif moeda == "ETH":
                saldo_eth -= (valor / cotacao)
            elif moeda == "XRP":
                saldo_xrp -= (valor / cotacao)
        else:
            saldo_att = saldo_anterior - valor

    with open(extrato, "a") as arquivo:
        arquivo.write(f"{data} {tipo}{valor:.2f} {moeda} CT: {cotacao:.2f}     TX: {taxa:.2f} REAL: {saldo_att:.2f} BTC: {saldo_bit:.6f} ETH: {saldo_eth:.6f} XRP: {saldo_xrp:.6f} \n")

def armazenar_bit():
    global precoBit

    if not os.path.exists(extrato):
        return 0.0
    
    with open(extrato, "r") as arquivo:
        saldo_bit = 0
    
        for linha in arquivo:
            if not linha.strip():
                continue
            linha_d = linha.split()
            valor = linha_d[2]
            moeda = linha_d[3]
            cotacao = float(linha_d[5])
            
            if moeda in ["REAL", "BTC", "ETH", "XRP"]:
                if moeda == "BTC":
                    if valor.find("+") == 0:
                        valor = float(valor.replace("+", ""))
                        saldo_bit += (valor / cotacao)

    
                    elif valor.find("-") == 0:
                        valor = float(valor.replace("-", ""))
                        saldo_bit -= (valor / cotacao)
                        
    return round(saldo_bit, 6)

def armazenar_eth():
    global precoEt

    if not os.path.exists(extrato):
        return 0.0
    
    with open(extrato, "r") as arquivo:
        saldo_eth = 0
    
        for linha in arquivo:
            if not linha.strip():
                continue
            linha_d = linha.split()
            valor = linha_d[2]
            moeda = linha_d[3]
            cotacao = float(linha_d[5])
            
            if moeda in ["REAL", "BTC", "ETH", "XRP"]:
                if moeda == "ETH":
                    if valor.find("+") == 0:
                        valor = float(valor.replace("+", ""))
                        saldo_eth += (valor / cotacao)

    
                    elif valor.find("-") == 0:
                        valor = float(valor.replace("-", ""))
                        saldo_eth -= (valor / cotacao)
                        
    return round(saldo_eth, 6)

def armazenar_xrp():
    global precoRip

    if not os.path.exists(extrato):
        return 0.0
    
    with open(extrato, "r") as arquivo:
        saldo_xrp = 0
    
        for linha in arquivo:
            if not linha.strip():
                continue
            linha_d = linha.split()
            valor = linha_d[2]
            moeda = linha_d[3]
            cotacao = float(linha_d[5])
            
            if moeda in ["REAL", "BTC", "ETH", "XRP"]:
                if moeda == "XRP":
                    if valor.find("+") == 0:
                        valor = float(valor.replace("+", ""))
                        saldo_xrp += (valor / cotacao)

    
                    elif valor.find("-") == 0:
                        valor = float(valor.replace("-", ""))
                        saldo_xrp -= (valor / cotacao)
                        
    return round(saldo_xrp, 6)


def armazenar_reais():

    if not os.path.exists(extrato):
        return 0.0
    
    with open(extrato, "r") as arquivo:
        saldo_att = 0

        for linha in arquivo:
            if not linha.strip():
                continue
            linha_d = linha.split()
            valor = linha_d[2]
            moeda = linha_d[3]
            taxa = linha_d[7]
        

            if moeda in ["REAL", "BTC", "ETH", "XRP"]:
                if valor.find("+") == 0:
                    if moeda != "REAL":
                        valor = float(valor.replace("+", ""))
                        valor_taxa = (valor * float(taxa))
                        saldo_att = saldo_att - (valor + valor_taxa)

                    else:
                        saldo_att = saldo_att + float(valor.replace("+", ""))

                elif valor.find("-") == 0:
                    valor = float(valor.replace("-", ""))
                    if moeda != "REAL":
                        valor_taxa = valor * float(taxa)
                        saldo_att = saldo_att + (valor - valor_taxa)

                    else:
                        saldo_att -= float(valor)
                    
    return round(saldo_att, 2)

def consultarExtrato():
    senha_def()

    print("\n" + "-" * 50)
    print("\nNome: Beatriz Cristina Braz Martins \nCPF: 123.456.789-10 \n")
    if not os.path.exists(extrato):
        print("Nenhuma operação registrada ainda.")
        print("\n" + "-" * 50)
        return

    with open(extrato, "r") as arquivo:
        for linha in arquivo.readlines():
            print(linha, end="")

    print("\n" + "-" * 50)


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

    print("\n" + "-" * 50)
    print("Cotação atual: \n")
    print(f"Bitcoin: R$ {precoBit:.2f}")
    print(f"Ethereum: R$ {precoEt:.2f}")
    print(f"Ripple: R$ {precoRip:.2f}")
    print("-" * 50)


def comprarCripto():
    global precoBit, precoEt, precoRip
    
    senha_def()

    print("\n" + "-" * 50)
    print("Cotações das Criptomoedas: \n")
    print(f"Bitcoin: R$ {precoBit:.2f}")
    print(f"Ethereum: R$ {precoEt:.2f}")
    print(f"Ripple: R$ {precoRip:.2f} \n")

    print("Qual das Criptomoedas gostaria de comprar? \n1 - Bitcoin \n2 - Ethereum \n3 - Ripple \n4 - Sair\n")
    compra = int(input())

    if compra == 1:
        qntd = float(input("Qual a quantidade em reais que gostaria de comprar? \nR$ "))
        saldo_atual = armazenar_reais()
        valor_taxa = qntd * 0.02
        qntd_total = qntd + valor_taxa

        if qntd_total <= saldo_atual:
            bitcoin = qntd / precoBit

            salvar(
                                tipo = "+",
                                valor = qntd,
                                moeda = "BTC",
                                cotacao = precoBit,
                                taxa = 0.02,
                                bitcoin = bitcoin,
                                ethereum = armazenar_eth(),
                                ripple = armazenar_xrp()
                    )
            
            print(f"Saldo atual após a compra (Reais): R$ {armazenar_reais():.2f}")
            
            print(f"\nVocê comprou {bitcoin:.6f } bitcoins!")

        else:
            print("Saldo insuficiente para a compra! \nDeposite mais reais para comprar.")


    elif compra == 2:
        qntd = float(input("Qual a quantidade em reais que gostaria de comprar? \nR$ "))
        saldo_atual = armazenar_reais()
        valor_taxa = qntd * 0.01
        qntd_total = qntd + valor_taxa

        if qntd_total <= saldo_atual:
            ethereum = qntd / precoEt

            salvar(
                    tipo = "+",
                    valor = qntd,
                    moeda = "ETH",
                    cotacao = precoEt,
                    taxa = 0.01,
                    bitcoin = armazenar_bit(),
                    ethereum = ethereum,
                    ripple = armazenar_xrp()
            )

            print(f"Saldo atual após a compra (Reais): R$ {armazenar_reais():.2f}")
                
            print(f"\nVocê comprou {ethereum:.6f} ethereums!")

        else:
            print("Saldo insuficiente para a compra! \nDeposite mais reais para comprar.")


    elif compra == 3:
        qntd = float(input("Qual a quantidade em reais que gostaria de comprar? \nR$ "))
        saldo_atual = armazenar_reais()
        valor_taxa = qntd * 0.01
        qntd_total = qntd + valor_taxa

        if qntd_total <= saldo_atual:
            ripple = qntd / precoRip

            salvar(
                    tipo = "+",
                    valor = qntd,
                    moeda = "XRP",
                    cotacao = precoRip,
                    taxa = 0.01,
                    bitcoin = armazenar_bit(),
                    ethereum = armazenar_eth(),
                    ripple = ripple
            )

            print(f"Saldo atual após a compra (Reais): R$ {armazenar_reais():.2f}")
                
            print(f"\nVocê comprou {ripple:.6f} ripples!")

        else:
            print("Saldo insuficiente para a compra! \nDeposite mais reais para comprar.")

    elif compra == 4:
        return

    else:
        return


def venderCripto():
    global precoBit, precoEt, precoRip

    senha_def()

    print("\n" + "-" * 50)
    print("Cotações das Criptomoedas: \n")
    print(f"Bitcoin: R$ {precoBit:.2f}")
    print(f"Ethereum: R$ {precoEt:.2f}")
    print(f"Ripple: R$ {precoRip:.2f} \n")

    print("Qual das Criptomoedas gostaria de vender? \n1 - Bitcoin \n2 - Ethereum \n3 - Ripple \n4 - Sair\n")
    venda = int(input())

    if venda == 1:
        print(f"Você possui {armazenar_bit():.6f} de Bitcoin \n")
        qntd = float(input("Qual a quantidade que gostaria de vender? "))
        saldo_bit = armazenar_bit()

        if qntd <= saldo_bit:
            valor_taxa = 0.03
            valor_reais = qntd * precoBit
            bitcoin = saldo_bit - qntd

            salvar(
                                tipo = "-",
                                valor = valor_reais,
                                moeda = "BTC",
                                cotacao = precoBit,
                                taxa = valor_taxa,
                                bitcoin = bitcoin,
                                ethereum = armazenar_eth(),
                                ripple = armazenar_xrp()
                    )            
    
            print(f"\nVocê vendeu {qntd:.6f} de bitcoins!")

        else:
            print("Saldo insuficiente para a venda!")


    if venda == 2:
        print(f"Você possui {armazenar_eth():.6f} de Ethereum \n")
        qntd = float(input("Qual a quantidade que gostaria de vender? "))
        saldo_eth = armazenar_eth()

        if qntd <= saldo_eth:
            valor_taxa = 0.02
            valor_reais = qntd * precoEt
            ethereum = saldo_eth - qntd

            salvar(
                                tipo = "-",
                                valor = valor_reais,
                                moeda = "ETH",
                                cotacao = precoEt,
                                taxa = valor_taxa,
                                bitcoin = armazenar_bit(),
                                ethereum = ethereum,
                                ripple = armazenar_xrp()
                    )            
    
            print(f"\nVocê vendeu {qntd:.6f} de ethereums!")

        else:
            print("Saldo insuficiente para a venda!")


    if venda == 3:
        print(f"Você possui {armazenar_xrp():.6f} de Ripple \n")
        qntd = float(input("Qual a quantidade que gostaria de vender? "))
        saldo_xrp = armazenar_xrp()

        if qntd <= saldo_xrp:
            valor_taxa = 0.01
            valor_reais = qntd * precoRip
            ripple = saldo_xrp - qntd

            salvar(
                                tipo = "-",
                                valor = valor_reais,
                                moeda = "XRP",
                                cotacao = precoRip,
                                taxa = valor_taxa,
                                bitcoin = armazenar_bit(),
                                ethereum = armazenar_eth(),
                                ripple = ripple
                    )            
    
            print(f"\nVocê vendeu {qntd:.6f} de ripples!")

        else:
            print("Saldo insuficiente para a venda!")

    elif venda == 4:
        return

    else:
        return


login()
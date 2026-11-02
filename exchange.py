
arquivo = "extrato.txt"
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
    print("Bem vindo ao menu! \nDigite a opção desejada! \n")
    print("1 - Consultar saldo")
    print("2 - Consultar extrato")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Comprar criptomoedas")
    print("6 - Vender criptomoedas")
    print("7 - Atualizar cotação")
    print("8 - Sair")

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


    
    
  






login()




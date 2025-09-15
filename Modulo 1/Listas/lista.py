cadastro = []

def cadastrar(cadastro):
    nome = input("Digite o nome: ")
    cadastro.append(nome)
    print(f"Usuário {nome} cadastrado ")

def listar(cadastro):
    nome = input("Digite o nome: ")
    cadastro.append(nome)
    print(f"Usuário {nome} listado ")

def excluir(cadastro):
    nome = input("Digite o nome: ")
    cadastro.remove(nome)
    print(f"Usuário {nome} exluido ")

while True:
    print("1 - Cadastrar usuario")
    print("2 - listar usuario")
    print("3 - remover usuario")
    opcao = input("Digite a opção: ")

    if opcao == "1":
        cadastrar(cadastro)

    elif opcao == "2":
        listar(cadastro)

    elif opcao == "3":
        excluir(cadastro)

    elif opcao == "0":
        break
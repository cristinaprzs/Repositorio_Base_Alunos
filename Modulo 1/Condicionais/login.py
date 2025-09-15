import time
print("-----------------------------")
print("********MERCADO LIVRE********")
print("-----------------------------")

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

print("Carregando...")
time.sleep(3)

if usuario == "admin" and senha == "1234":
    print("-----------------------------")
    print("Login bem-sucedido!")
    print("-----------------------------")
    print(f"Bem-vindo ao Mercado Livre {usuario}!")
else:
    print("Usuário ou senha incorretos.")
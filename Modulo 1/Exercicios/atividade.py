mínimo = int(input("Digite o valor mínimo: "))
máximo = int(input("Digite o valor máximo: "))
multiplicador = int(input("Digite o número do multiplicador: "))

for i in range(mínimo,máximo +1):
    print(f" {i} x {multiplicador} = {i * multiplicador}")
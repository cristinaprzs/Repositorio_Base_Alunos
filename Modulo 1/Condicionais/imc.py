try:
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso/(altura*altura)
    print(f"O índice de massa corporal do paciente {nome} é: {imc:.2f} ")

    if imc <18.5:
        print("Abaixo do peso ideal")

    if imc >= 18.6 and imc <=24.9:
        print("Peso ideal")

    if imc >= 25.0 and imc <=29.9:
        print("Sobrepeso")

    if imc >= 30.0 and imc <=34.9:
        print("Obesidade grau 1")

    if imc >= 35.0 and imc <=39.9:
        print("Obesidade grau 2")

    if imc >= 40.0:
        print("Obesidade grau 3")
except:
    print("Valor incorreto-")

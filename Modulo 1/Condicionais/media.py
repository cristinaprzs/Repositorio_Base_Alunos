nome = input("Digite o nome do aluno: ")

Nota1 = float(input("Digite sua primeira nota: "))
Nota2 = float(input("Digite sua segunda nota: "))
Nota3 = float(input("Digite sua terceira nota: "))

Média = (Nota1 + Nota2 + Nota3) / 3

if Média >= 7:
    print("Muito bem, aprovado! ")
elif Média >= 4:
    print("Não foi goti, ta de recuperação X.X ")
else:
    print("Ta de sacas? Reprovado irmão")

print(f"A média do aluno {nome} é {Média}")
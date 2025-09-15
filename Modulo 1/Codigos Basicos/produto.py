nome_produto = input("digite o nome do nome produto:")
preco =float(input("digite o preco do produto:R$"))
desconto =float(input("digite o perecwentual de desconto % :"))

valor_desconto = preco * desconto/100

preco_final= preco - valor_desconto 
print("-----------------------------")
print(f"prduto:{nome_produto}\nPreço final:{preco_final}")
print("-------------------------------")
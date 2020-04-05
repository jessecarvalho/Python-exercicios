valorProduto = int(input("Digite o valor do produto a ser comprado: "))
desconto = int(input("Digite o desconto a ser aplicado: "))
valorProdutoComDesc = valorProduto - ((valorProduto / 100) * desconto)
print(f"O produto com desconto de {desconto}% fica: R${valorProdutoComDesc}")
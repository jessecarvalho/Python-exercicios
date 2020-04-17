# Objetivo do algorítmo:
# O usuário deverá digitar o valor do produto 
# e em seguida o valor do desconto a ser aplicado.
# O algorítimo deverá calcular o valor com o desconto.
# Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo


def calculaDec(valorProduto, desconto):
    valorProdutoComDesc = valorProduto - ((valorProduto / 100) * desconto)
    print(f"O produto com desconto de {desconto}% fica: R${valorProdutoComDesc}")

if __name__ == '__main__':
    valorProduto = int(input("Digite o valor do produto a ser comprado: "))
    desconto = int(input("Digite o desconto a ser aplicado: "))
    calculaDec(valorProduto, desconto)
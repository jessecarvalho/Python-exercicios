# Objetivo do algoritimo:
# Escrever um algoritmo para aprovar um empréstimo bancário para a compra de uma casa.
# O algoritimo deverá perguntar o valor da casa, o salario do comprador e em quantos anos irá pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
# Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo

valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário: "))
anos = int(input("Em quantos anos irá pagar? "))
meses = anos * 12
mensalidade = valorCasa / meses
limiteMaximo = (salario / 100) * 30
if limiteMaximo < mensalidade:
    print("Empréstimo não aprovado!")
else:
    print("Empréstimo aprovado com sucesso!")
    print(f"A mensalidade ficará no custo de R${mensalidade}")
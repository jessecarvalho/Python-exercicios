# Objetivo do algorítimo:
# O algortimo deverá pedir o valor em reais a ser convertido para dólar.
# O algoritimo deverá calcular o valor em dólar baseado em um valor estático
# Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo

def conversor(dolar):
    real = dolar * 5.35
    print(f'Com R${dolar} você consegue comprar ${real}')

if __name__ == '__main__':
    dolar = int(input("Digite o valor a ser convertido em real: R$"))
    conversor(dolar)
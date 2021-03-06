# Objetivo do algorítimo:
# Desenvolver um programa que pergunte a distância de uma viagem em Km.
# Calcular o preço da passagem cobrando R$0.50 por Km para viagens de até 
# 200km e R$0.45 por viagens mais longas.
# Exercicio pensado por: Gustavo Guanabará / Curso em vídeo

def calculaCusto(distancia):
    if distancia < 200 and distancia > 0:
        valorPassagem = distancia * 0.50
    elif distancia > 200:
        valorPassagem = distancia * 0.45
    else:
        print("Valor inválido digitado")
    print(f"O valor da passagem de {distancia}Km ficou em: R${valorPassagem}")
    
if __name__ == '__main__':
    distancia = int(input("Digite a distância em Km: "))
    calculaCusto(distancia)

# Objetivo do algorítimo:
# Escrever um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa deverá custar 7 reais por cada KM acima do limite.
# Exercicio pensado por: Gustavo Guanabara / Curso em vídeo

def radar(actual, limit):
    if actual > limit:
        print("MULTADO: você excedeu o limite de velocidade permitido")
        trafficTicket = (actual - limit) * 7
        print(f"O valor de sua multa ficou em: R${trafficTicket}")

if __name__ == '__main__':
    actualVelocity = int(input("Digite a velocidade atual do carro: "))
    limitVelocidade = int(input("Diga-me a velocidade máxima permitida: "))
    radar(actualVelocity, limitVelocidade)


    
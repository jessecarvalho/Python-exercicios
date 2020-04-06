#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa deverá custar 7 reais por cada KM acima do limite.
#Exercicio pensado por: Gustavo Guanabara / Curso em vídeo


velocidadeAtual = int(input("Digite a velocidade atual do carro: "))
limiteVelocidade = 80
if velocidadeAtual > limiteVelocidade:
    print("MULTADO: você excedeu o limite de velocidade permitido")
    valorMulta = (velocidadeAtual - limiteVelocidade) * 7
    print(f"O valor de sua multa ficou em: R${valorMulta}")
    
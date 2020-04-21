#Faça um programa que mostre uma contagem regressiva
#para estouro de fogos de artificio.
# Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo

from time import sleep

def countdown(initial):
    if initial >= 0:
        print(initial)
        initial -= 1
        sleep(1)
        countdown(initial)
    else:
        print("Fim da contagem!")


if __name__ == '__main__':
    countdown(10)
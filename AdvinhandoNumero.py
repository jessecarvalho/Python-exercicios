# Objetivo do algoritimo:
# O programa deverá pensar em um número.
# O usuário terá 5 chances de advinhar o número.
# O programa deverá dar dicas ao usuário.
# Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo
from random import randint
from time import sleep

def trying(numero, tentativas):
    while True: 
        advinhado = int(input("> "))
        if advinhado == numero:
            print("Você acertou, parabéns!")
            break
        else:
            "Você errou!"
            sleep(1)
            if advinhado > numero:
                print("Tente um numero mais abaixo")
            else:
                print("tente um numero mais acima")
            sleep(1)
            tentativas = tentativas - 1
            if(tentativas > 0):
                print(f"Você tem apenas mais {tentativas} tentativas")
            else:
                print("Game Over")
                break;

def guess():
    return randint(1,100)

def dificuldade():
    dificuldade = int(input(">"))
    if dificuldade == 1:
        return 5
    if dificuldade == 2:
        return 3
    else:
        print ("Você digitou um valor errado, tente novamente!")
        dificuldade()

if __name__ == '__main__':
    guess();
    print("Bem vindo ao jogo da advinhação.")
    sleep(1.5)
    print("Irei pensar em um número de 1 a 100 e você, com minhas dicas deverá advinha-lo")
    sleep(2)
    print("Em qual nível você quer jogar? 1 para fácil e 2 para dificil")
    tentativas = dificuldade()
    sleep(2)
    print('Tudo certo... huumm...')
    sleep(1.5)
    numero = guess()
    print('Número pensado, vamos lá. Tente acertar')
    trying(numero, tentativas)
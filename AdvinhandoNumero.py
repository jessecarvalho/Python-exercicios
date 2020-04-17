# Objetivo do algoritimo:
# O programa deverá pensar em um número.
# O usuário terá 5 chances de advinhar o número.
# O programa deverá dar dicas ao usuário.
# Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo

def trying():
    

def guess():
    from random import randint
    from time import sleep
    tentativas = 5
    print("Bem vindo ao jogo da advinhação.")
    sleep(1.5)
    print("Irei pensar em um número de 1 a 100 e você, com minhas dicas deverá advinha-lo")
    sleep(2)
    print('hmmmm....')
    sleep(1.5)
    numero = randint(1,100)
    print('Número pensado, vamos lá. Tente acertar')
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
        
if __name__ == '__main__':
    guess();
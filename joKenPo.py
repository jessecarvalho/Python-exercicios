# Objetivo do algorítimo:
# Desenvolver o clássico joKenPo.
# Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo
from random import randint

def shot():
    print('Suas opções: ')
    print('[0] Pedra')
    print('[1] Papel')
    print('[2] tesoura')
    print('Qual a sua jogada?')
    move = int(input('>'))
    movePc = randint(0,2)
    plays = [move, movePc]
    return plays
    

def tester(move):
    if (move == 0 or move == 1 or move == 2):
        return True;
    else:
        print("Jogada invalida, tente novamente")
        shot();

def play(move, movePc):
    if move == 0:
        if movePc == 0:
            print('Você jogou pedra')
            print('O computador jogou pedra')
            print('Deu empate!')
        if movePc == 1:
            print('Você jogou pedra')
            print('O computador jogou papel')
            print('Você perdeu!')
        if movePc == 2:
            print('Você jogou pedra') 
            print('O computador jogou tesoura')
            print('Você ganhou!')
    elif move == 1:
        if movePc == 0:
            print('Você jogou papel')
            print('O computador jogou pedra')
            print('Você ganhou!')
        if movePc == 1:
            print('Você jogou papel')
            print('O computador jogou papel')
            print('Deu empate!')
        if movePc == 2:
            print('Você jogou papel')
            print('O computador jogou tesoura')
            print('Você perdeu!')
    elif move == 2:
        if movePc == 0:
            print('Você jogou tesoura')
            print('O computador jogou pedra')
            print('Você perdeu!')
        if movePc == 1:
            print('Você jogou tesoura')
            print('O computador jogou papel')
            print('Você ganhou!')
        if movePc == 2:
            print('Você jogou tesoura')
            print('O computador jogou tesoura')
            print('Deu empate!')

if __name__ == '__main__':
    plays = shot()
    tester = tester(plays[0])
    play = play(plays[0], plays[1]);
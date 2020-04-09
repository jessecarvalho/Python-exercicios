from random import randint

print('Suas opções: ')
print('[0] Pedra')
print('[1] Papel')
print('[2] tesoura')
print('Qual a sua jogada?')
jogada = int(input('>'))
jogadaPc = randint(0,2)
if jogada == 0:
    if jogadaPc == 0:
        print('Você jogou pedra')
        print('O computador jogou pedra')
        print('Deu empate!')
    if jogadaPc == 1:
        print('Você jogou pedra')
        print('O computador jogou papel')
        print('Você perdeu!')
    if jogadaPc == 2:
        print('Você jogou pedra') 
        print('O computador jogou tesoura')
        print('Você ganhou!')
elif jogada == 1:
    if jogadaPc == 0:
        print('Você jogou papel')
        print('O computador jogou pedra')
        print('Você ganhou!')
    if jogadaPc == 1:
        print('Você jogou papel')
        print('O computador jogou papel')
        print('Deu empate!')
    if jogadaPc == 2:
        print('Você jogou papel')
        print('O computador jogou tesoura')
        print('Você perdeu!')
elif jogada == 2:
    if jogadaPc == 0:
        print('Você jogou tesoura')
        print('O computador jogou pedra')
        print('Você perdeu!')
    if jogadaPc == 1:
        print('Você jogou tesoura')
        print('O computador jogou papel')
        print('Você ganhou!')
    if jogadaPc == 2:
        print('Você jogou tesoura')
        print('O computador jogou tesoura')
        print('Deu empate!')

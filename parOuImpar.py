# Objetivo do algorítimo:
# Desenvolver o clássico Par Ou Impar
# Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo

def play(number):
    if number % 2 == 1:
        print("Este é um número impar!")
    else:
        print("Este é um número par!")
    

if __name__ == '__main__':
    number = int(input("Me diga um número: "))
    play(number);
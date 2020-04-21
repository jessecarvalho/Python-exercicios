# Objetivo do algorítimo:
# Desenvolver um programa para a aciociação de nacional de Natação
# que leia o ano de nascimento do atleta e mostre sua categoria
# de acordo com idade.
# Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo


from datetime import date

def classification(birthYear):
    todayDate = date.today().year
    yearsOld = todayDate - birthYear
    if yearsOld > 0 and yearsOld <= 9:
        print("Mirim")
    elif yearsOld <= 14:
        print("Infantil")
    elif yearsOld <= 19:
        print("Junior")
    elif yearsOld <= 25:
        print("Sênior")
    elif yearsOld > 25 and yearsOld < 150:
        print("Master")
    else:
        print("Data de nascimento inválida!")


if __name__ == '__main__':
    classification(int(input("Por favor, digite seu ano de nascimento!")))

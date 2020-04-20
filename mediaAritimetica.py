# Objetivo do algorítimo:
# Usuário deve ser capaz de escolher a quantidade de notas
# Usuário deve ser capaz de inserir as notas
# Programa deve calcular a média final
#Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo

def calcAvg(gradesAmount):
    i = 1
    grades = []
    sumGrades = 0
    while i <= gradesAmount:
        grades.append(int(input(f'Digite a {i}ª nota:')))
        i += 1
    for grade in grades:
        sumGrades += grade
    average = sumGrades / gradesAmount
    print(f'A média final é: {average}')


if __name__ == '__main__':
    gradesAmount = int(input('digite a quantidade de notas que serão calculadas: '))
    calcAvg(gradesAmount)

# Usuário deve ser capaz de solicitar tabuada de determinado número
# Programa deve oferecer tabuada ao usuário

def multiplicationTable(num):
    i = 0
    print(f'--TABUADA DO {num} ')
    while i <= 10:
        calc = i * num
        print(f'{num} * {i} = {calc}')
        i += 1
if __name__ == '__main__':
    multiplicationTable(int(input('Digite um número para ver a tabuada: ')));
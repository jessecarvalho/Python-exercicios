# Usuário deve ser capaz de solicitar tabuada de determinado número
# Programa deve oferecer tabuada ao usuário
i = 0
num = int(input('Digite um número para ver a tabuada: '))
print(f'--TABUADA DO {num} ')
while i <= 10:
    calc = i * num
    print(f'{num} * {i} = {calc}')
    i += 1
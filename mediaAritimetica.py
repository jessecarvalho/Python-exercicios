# Usuário deve ser capaz de escolher a quantidade de notas
# Usuário deve ser capaz de inserir as notas
# Programa deve calcular a média final


quantidadeNotas = int(input('digite a quantidade de notas que serão calculadas: '))
i = 1
notas = []
somaNotas = 0
while i <= quantidadeNotas:
    notas.append(int(input(f'Digite a {i}ª nota:')))
    i += 1
for nota in notas:
    somaNotas += nota
media = somaNotas / quantidadeNotas
print(f'A média final é: {media}')
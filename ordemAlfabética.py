# Objetivo do algorítimo:
# Criar uma lista em ordem alfabética a partir de uma lista dada pelo usuário.
# Exercício pensado por mim mesmo.

lista = []
decisao = True
while decisao == True:
    lista.append(input('Digite o item '))
    print('Deseja parar a adição de itens? caso sim digite "s" ')
    print('Caso não, digite qualquer outro botão ')
    decisao = input('')
    if decisao == 's':
        decisao = False;
    else:
        decisao = True;
lista.sort()
print(lista)

# Objetivo do algorítimo:
# Criar uma lista em ordem alfabética a partir de uma lista dada pelo usuário.
# Exercício pensado por mim mesmo.

def listOrdem():
    theList = []
    decision = True
    while decision == True:
        theList.append(input('Digite o item '))
        print('Deseja parar a adição de itens? caso sim digite "s" ')
        print('Caso não, digite qualquer outro botão ')
        decision = input('')
        if decision == 's':
            decision = False;
        else:
            decision = True;
    theList.sort()
    print(theList)

if __name__ == '__main__':
    listOrdem();
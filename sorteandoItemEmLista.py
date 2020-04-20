# Objetivo do algorítimo:
# Desenvolver um algoritimo que pegue valores de uma lista e faça um sorteio
# Exercicio pensado por: Gustavo Guanabará / Curso Em Vídeo

from random import randint

def addItens():
    theList = []
    while True:
        item = input('Adicione um item à lista: ')
        theList.append(item)
        breaker = input('Já adicionou todos itens? (S para sim, N para não)')
        if breaker == "s":
            return theList;

def sortItem(theList):
    ramdomValue = randint(0,len(theList)-1)
    selecionado = theList[ramdomValue]
    print(f"O valor selecionado é: {selecionado}")


if __name__ == '__main__':
    theList = addItens();
    sortItem(theList);
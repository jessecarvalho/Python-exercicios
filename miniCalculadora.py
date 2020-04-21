
def calc(choice, theList):
    if choice == 1:
        print(int(theList[0]) + int(theList[1]))
        run()
    elif choice == 2:
        print(int(theList[0]) * int(theList[1]))
        run()
    elif choice == 3:
        if int(theList[0]) > int(theList[1]):
            print(f'{theList[0]} é o maior')
            run()
        else:
            print(f'{theList[1]} é o maior')
            run()
    elif choice == 4:
        run()
    elif choice == 5:
        print("Até mais!")


def choseValues(theList):
    value = input("Digite um número: ")
    return value


def values():
    theList = []
    for i in range(0, 2):
        theList.append(choseValues(theList))
    return theList


def options():
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")
    return int(input("Escolha uma opção: "))


def run():
    theList = values()
    choice = options()
    calc(choice, theList)


if __name__ == "__main__":
    run()
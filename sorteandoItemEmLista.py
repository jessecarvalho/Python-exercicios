from random import randint

lista = []
while True:
    item = input('Adicione um item à lista: ')
    lista.append(item)
    breaker = input('Já adicionou todos itens? (S para sim, N para não)')
    if breaker == "s":
        break;
aleatorio = randint(0,len(lista)-1)
selecionado = lista[aleatorio]
print(f"O valor selecionado é: {selecionado}")

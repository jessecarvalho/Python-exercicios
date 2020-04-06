#Desenvolver uma lógica que leia a altura e o peso de uma pessoa
#calcule seu imc e mostre seu status de acordo com a tabela:
#Abaixo de 18.5: Abaixo do peso.
#Entre 18.5 e 25: Peso ideal.
#25 até 30: Sobrepeso.
#30 até 40: Obesidade
#Acima de 40 obesidade mórbida
#Exercicio pensado por: Gustavo Guanabara / Curso em vídeo

peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("QUal é sua altura? (m) "))
imc = peso / (altura*altura)
print(f'O seu imc é: {imc}')
if imc < 18.5:
    print("Você está no peso ideal!")
elif imc >= 18.5 and imc < 25:
    print("Você está no seu peso ideal")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso")
elif imc >=30 and imc < 40:
    print('Você está com obesidade')
elif imc > 40:
    print('Você está com obesidade mórbida')

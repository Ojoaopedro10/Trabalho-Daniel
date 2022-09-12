#6 - Faça um programa que calcule e mostre a área de um triângulo. Sabe-se que: Área = (base*altura)/2.
base = float(input('Digite a base do seu triângulo: '))
altura = float(input('Digite a altura do triângulo: '))
area = (base * altura)/2
print('A área do seu triângulo é: {:.2f}'.format(area))
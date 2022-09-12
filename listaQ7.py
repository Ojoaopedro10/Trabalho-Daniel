#7 - Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga impostoo de 7% também sobre o salário base.
sal = int(input('Informe o salário: '))
saltotal = sal + 0.05*sal - 0.07*sal
print("O salário a receber é {:.2f}".format(saltotal))
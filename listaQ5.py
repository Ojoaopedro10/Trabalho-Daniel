#5 - Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
sal = int(input('Informe seu salário: '))
aumento = int(input('Informe seu aumento em porcentagem: '))
saltotal = (aumento / 100 *sal) + sal
print('aumento: {:.2f}'.format(aumento /100 * sal))
print('novo salario: {:.2f}'.format(saltotal))
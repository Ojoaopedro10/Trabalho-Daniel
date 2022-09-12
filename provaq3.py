#3 - Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
    #a) A idade dessa pessoa;
    #b) Quantos anos ela terá em 2050.
anonascimento = float(input('digite em que ano você nasceu: '))
ano = float(input('Digite em que ano estamos: '))
idade = ano - anonascimento
idadedois = 2050 - anonascimento
print('A sua idade é: ',idade)
print('A sua idade em 2050 seria: ',idadedois)
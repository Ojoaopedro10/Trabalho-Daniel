#03 - LISTA DE EXERCÍCIOS

nota001 = float (input("Primeira nota: "))

nota002 = float (input("Segunda nota: "))

nota003 = float (input("Terceira nota: "))

peso001 = float (input("Primeiro peso: "))

peso002 = float (input("Segundo peso:"))

peso003 = float (input("Terceiro peso: "))

operacao001 = nota001*peso001 + nota002*peso002 + nota003*peso003

operacao002 = peso001+peso002+peso003

operacao003 = operacao001/operacao002

print('Resultado: {:.2f}'.format(operacao003))
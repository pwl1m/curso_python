#aula sobre f-string (formatação de string)
nome = 'Diana Maria'
altura = 1.70
peso = 65
imc = peso/altura ** 2

linha1 = f'{nome} tem: {altura:.2f}cm' #2f paga gerar casa 2 casas decimais
linha2 = f'pesa: {peso}kg'
linha3 = f'tem o imc:{imc: .2f}'

print(linha1)
print(linha2)
print(linha3)
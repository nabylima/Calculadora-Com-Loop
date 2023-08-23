operacao = input('''
Digite a operação matemática desejada:
+ para Soma
- para Subtração
* para Multiplicação
/ para Divisão
''')


numero_1 = int(input("Insira seu primeiro número: "))
numero_2 = int(input("Insira seu segundo número: "))

if operacao == '+':
  print('{}+{} = '.format(numero_1, numero_2))
  print("O Resultado da soma é:", numero_1 + numero_2)

elif operacao == '-':
  print('{}-{} = '.format(numero_1, numero_2))
  print("O Resultado da subtração é:", numero_1 - numero_2)

elif operacao == '*':
  print('{}*{} = '.format(numero_1, numero_2))
  print("O Resultado da multiplicação é:", numero_1 * numero_2)

elif operacao == '/':
  print('{}/{} = '.format(numero_1, numero_2))
  print("O Resultado da divisão é:", numero_1 / numero_2)

else:
  print("Essa opção não existe!")

operacao = ""
while (operacao != "Sim"):
  print("Digite Sim se deseja sair da operação!")
  operacao = str(input())
  print("Operação Finalizada!!!")
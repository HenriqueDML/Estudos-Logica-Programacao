# 1. Peça um número ao usuário e exiba se ele é par ou ímpar.
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 2. Solicite um número ao usuário e verifique se ele é positivo, negativo ou zero.
num = int(input("Digite um número: "))
if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# 3. Peça ao usuário dois números e exiba o maior.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os dois números são iguais.")

# 4. Crie um programa que peça uma senha ao usuário. Se a senha for "1234", exiba "Acesso permitido", senão, "Acesso negado".
senha = input("Digite a senha: ")
if senha == "1234":
    print("Acesso permitido.")
else:
    print("Acesso negado.")

# 5. Crie um menu onde o usuário pode escolher entre:
#    1. Somar dois números
#    2. Subtrair dois números
#    3. Multiplicar dois números
#    4. Dividir dois números
#    O programa deve executar a opção escolhida e mostrar o resultado.
print("Escolha uma opção:")
print("1. Somar dois números")
print("2. Subtrair dois números")
print("3. Multiplicar dois números")
print("4. Dividir dois números")
opcao = int(input("Digite o número da opção desejada: "))

if opcao in [1, 2, 3, 4]:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        print("Resultado:", num1 + num2)
    elif opcao == 2:
        print("Resultado:", num1 - num2)
    elif opcao == 3:
        print("Resultado:", num1 * num2)
    elif opcao == 4:
        if num2 == 0:
            print("Erro: Divisão por zero não permitida.")
        else:
            print("Resultado:", num1 / num2)
else:
    print("Opção inválida.")

# 6. Faça um programa que pergunte a idade do usuário e informe se ele é menor de idade (menos de 18), adulto (entre 18 e 60) ou idoso (mais de 60).
idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Você é menor de idade.")
elif idade <= 60:
    print("Você é adulto.")
else:
    print("Você é idoso.")

# 7. Peça ao usuário um número de 1 a 7 e exiba o dia da semana correspondente.
dias = ["", "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
num = int(input("Digite um número de 1 a 7: "))
if 1 <= num <= 7:
    print("O dia da semana é:", dias[num])
else:
    print("Número inválido! Digite um número entre 1 e 7.")

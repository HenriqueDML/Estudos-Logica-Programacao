import random

# 1
numeros = [int(input("Digite um número: ")) for _ in range(10)]
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))

# 2
import string
senha = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print("Senha gerada:", senha)

# 3
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"Fahrenheit: {fahrenheit:.2f}, Kelvin: {kelvin:.2f}")

# 4
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = sum(1 for letra in frase if letra in vogais)
print("Quantidade de vogais:", contador)

# 5
pessoas = []
for _ in range(3):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("E-mail: ")
    pessoas.append({"nome": nome, "idade": idade, "email": email})
print("Pessoas cadastradas:", pessoas)

# 6
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    return True

cpf = input("Digite um CPF: ")
print("CPF válido!" if validar_cpf(cpf) else "CPF inválido!")

# 7
numero_secreto = random.randint(1, 100)
tentativa = 0
while True:
    tentativa += 1
    palpite = int(input("Adivinhe o número: "))
    if palpite < numero_secreto:
        print("Tente um número maior.")
    elif palpite > numero_secreto:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou em {tentativa} tentativas.")
        break

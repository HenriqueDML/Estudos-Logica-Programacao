# 1
num = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 2
num = int(input("Digite um número: "))
i = 0
while i <= num:
    print(i)
    i += 2

# 3
numeros = []
for i in range(5):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))
print("Soma:", sum(numeros))

# 4
lista = [10, 20, 30, 40, 50]
num = int(input("Digite um número: "))
if num in lista:
    print("O número está na lista!")
else:
    print("O número não está na lista.")

# 5
num = int(input("Digite um número: "))
a, b = 0, 1
while a <= num:
    print(a, end=" ")
    a, b = b, a + b
print()

# 6
palavra = input("Digite uma palavra: ")
print("Invertida:", palavra[::-1])

# 7
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite um número para [{i}][{j}]: ")))
    matriz.append(linha)

for linha in matriz:
    print(linha)

numero = int(input("Digite um número inteiro: "))

print("Números pares de 0 até", numero, ":")
for i in range(0, numero + 1):
    if i % 2 == 0:
        print(i)

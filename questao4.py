
entrada = input("Digite uma lista de números separados por espaço: ")


numeros = list(map(int, entrada.split()))


if numeros:
    
    maior = max(numeros)
    menor = min(numeros)

    
    print(f"O maior valor da lista é: {maior}")
    print(f"O menor valor da lista é: {menor}")
else:
    print("A lista está vazia. Não há valores para comparar.")
